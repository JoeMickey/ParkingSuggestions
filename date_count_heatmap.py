import pandas as pd
import datetime as dt
import numpy as np 
import seaborn as sn
import matplotlib.pyplot as plt 



def parse_cols_basic():
    '''
    Combines all of the file data and lists the amount of citations per day in order
    Make sure to change the read paths for the .csv files
    '''

    read_list_rev = ['parking_citations_2012_part1_datasd.csv', 'parking_citations_2012_part2_datasd.csv',
                'parking_citations_2013_part1_datasd.csv', 'parking_citations_2013_part2_datasd.csv',
                'parking_citations_2014_part1_datasd.csv', 'parking_citations_2014_part2_datasd.csv',
                'parking_citations_2015_part1_datasd.csv', 'parking_citations_2015_part2_datasd.csv',
                'parking_citations_2016_part1_datasd.csv', 'parking_citations_2016_part2_datasd.csv',
                'parking_citations_2017_part1_datasd.csv', 'parking_citations_2017_part2_datasd.csv',
                'parking_citations_2018_part1_datasd.csv', 'parking_citations_2018_part2_datasd.csv',
                ]
    read_list_norm = ['parking_citations_2019_part1_datasd.csv', 'parking_citations_2019_part2_datasd.csv',
                'parking_citations_2020_part1_datasd.csv', 'parking_citations_2020_part2_datasd.csv',
                'parking_citations_2021_part1_datasd.csv', 'parking_citations_2021_part2_datasd.csv',
                'parking_citations_2022_part1_datasd.csv', 'parking_citations_2022_part2_datasd.csv',
                'parking_citations_2023_part1_datasd.csv', 'parking_citations_2023_part2_datasd.csv'
                ]
    
    con_list = []
    for f in read_list_rev:
        df = pd.read_csv('python_read_files/' + f) # make sure to change this to the correct python read path
        df = df.reindex(index=df.index[::-1])
        con_list.append(df)
    for f in read_list_norm:
        df = pd.read_csv('python_read_files/' + f) # make sure to change this to the correct python read path
        con_list.append(df)
    output_df = pd.concat(con_list)
    return output_df




def date_count(df):
    '''
    Returns a dataframe consisting of the date and number of parking citations.
    df: dataframe with parking citation data, relies on information being in order.
    '''
    assert isinstance(df, pd.DataFrame)

    date_dict = {}
    output_DF = pd.DataFrame()
    dates = df['date_issue'].to_list()
    for date in dates:
        if not date in date_dict.keys():
            date_dict[date] = 1
        else:
            date_dict[date] += 1
    output_DF.index = date_dict.keys()
    output_DF['count'] = date_dict.values()
    return output_DF


def parse_cols_month(df):
    '''
    Combines all of the month's parking citations.
    df: sorted dataframe from parse_data()
    '''
    assert isinstance(df, pd.DataFrame)

    m = -1
    y = -1
    sum_count = 0
    temp_dict = {}
    for date in df.index:  
        datee = dt.datetime.strptime(date, "%Y-%m-%d")
        if m == -1 or y == -1:
            m = datee.month
            y = datee.year
        if datee.month == m and datee.year == y:
            sum_count += df.loc[date, 'count']
        else:
            temp_dict[str(y) + '-' + str(m)] = sum_count
            m = -1
            y = -1
            sum_count = df.loc[date, 'count']
        if datee.month == 10 and datee.year == 2023: # covers edge case on last iteration
            temp_dict[str(2023) + '-' + str(10)] = sum_count
    output_DF = pd.DataFrame()
    output_DF.index = temp_dict.keys()
    output_DF['count'] = temp_dict.values()
    return output_DF


def parse_cols_year(df):
    '''
    Lists the parking citation count by month (rows) and by year (columns).
    df: output dataframe of parse_cols_month(df)
    '''
    assert isinstance(df, pd.DataFrame)

    y = -1
    m_in_same_y = []  
    output_DF = pd.DataFrame()
    for date in df.index:
        datee = dt.datetime.strptime(date, "%Y-%m")   
        if y == -1:
            y = datee.year
        if datee.year == y:
            m_in_same_y.append(df.loc[date, 'count'])
        else:
            output_DF[str(y)] = m_in_same_y
            y = -1
            m_in_same_y = [] 
            m_in_same_y.append(df.loc[date, 'count'])
        if datee.month == 10 and datee.year == 2023: # covers edge case on last iteration, November and December have not passed
            m_in_same_y.append(None)
            m_in_same_y.append(None)
            output_DF[str(2023)] = m_in_same_y
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    output_DF.index = month_names

    return output_DF


def parse_cols_daily(month, df):
    '''
    Cuts out all data besides the ones listed for a particular month.
    month: month to capture data from
    df: dataframe with parking citation data 
    '''
    assert isinstance(month, int) and isinstance(df, pd.DataFrame)
    assert 1<=month<=12

    temp_dict = {}
    for date in df.index:  
        datee = dt.datetime.strptime(date, "%Y-%m-%d")
        if datee.month == month:
            d = datee.day
            y = datee.year
            m = datee.month
            temp_dict[str(y) + '-' + str(m) + '-' + str(d)] = df.loc[date, 'count']
    output_DF = pd.DataFrame()
    output_DF.index = temp_dict.keys()
    output_DF['count'] = temp_dict.values()
    return output_DF


def parse_cols_daily2(df):
    '''
    Lists the parking citation count by day (rows) and by year (columns).
    df: output dataframe of parse_cols_daily(df)
    '''
    assert isinstance(df, pd.DataFrame)

    y = -1
    d_in_same_y = []  
    output_DF = pd.DataFrame()
    month = 0
    for date in df.index:
        datee = dt.datetime.strptime(date, "%Y-%m-%d")   
        month = datee.month
        if y == -1:
            y = datee.year
        if datee.year == y:
            d_in_same_y.append(df.loc[date, 'count'])
        else:
            if len(d_in_same_y) == 28:
                d_in_same_y.append(None)
            output_DF[str(y)] = d_in_same_y
            y = -1
            d_in_same_y = [] 
            d_in_same_y.append(df.loc[date, 'count'])

    if len(d_in_same_y) == 28: # to catch edge case of last year
        d_in_same_y.append(None)    
    output_DF[str(y)] = d_in_same_y

    if month==4 or month==6 or month==9 or month==11:
        day_list = range(1,31)
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        day_list = range(1,32)
    else:
        day_list = range(1,30)
    output_DF.index = day_list

    return output_DF


def time_heatmap(df):
    '''
    Parses the dataframe and plots time series heatmaps for the months of October, November, December
    and for all the months over the years.
    df: dataframe with parking citation data
    '''
    assert isinstance(df, pd.DataFrame)

    df = date_count(df)

    pcm = parse_cols_month(df)
    pcy = parse_cols_year(pcm)

    pcd_10 = parse_cols_daily(10,df)
    pcd_o = parse_cols_daily2(pcd_10)

    pcd_11 = parse_cols_daily(11,df)
    pcd_n = parse_cols_daily2(pcd_11)

    pcd_12 = parse_cols_daily(12,df)
    pcd_d = parse_cols_daily2(pcd_12)
    
    data_m = pcy.to_numpy()
    data_oct = pcd_o.to_numpy()
    data_nov = pcd_n.to_numpy()
    data_dec = pcd_d.to_numpy()


    x_axis_labels = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    y_axis_labels_12 = ['January', 'February','March','April','May','June','July','August','September',
                        'October','November','December']
    y_axis_lables_31 = list(range(1,32))

    cmap = sn.cm.rocket_r
    # plotting the heatmap for months
    hm = sn.heatmap(data_m, xticklabels=x_axis_labels, yticklabels=y_axis_labels_12, cmap = cmap) 
    # displaying the plotted heatmap 
    plt.show()

    # plotting the heatmap for October
    hq = sn.heatmap(data_oct, xticklabels=x_axis_labels, yticklabels=y_axis_lables_31, cmap=cmap) 
    # displaying the plotted heatmap 
    plt.show()

    # plotting the heatmap for October
    hq = sn.heatmap(data_nov, xticklabels=x_axis_labels, yticklabels=y_axis_lables_31, cmap=cmap) 
    # displaying the plotted heatmap 
    plt.show()

    # plotting the heatmap for October
    hq = sn.heatmap(data_dec, xticklabels=x_axis_labels, yticklabels=y_axis_lables_31, cmap=cmap) 
    # displaying the plotted heatmap 
    plt.show()

def main(df): #for file imports, call 
    '''
    Creates the relevant heatmaps for ECE 143 Final Project
    df: dataframe with parking citation data in order in time
    '''
    assert isinstance(df, pd.DataFrame)

    time_heatmap(df)

# conditional for main
#if __name__ == "__main__":
#    main()