import pandas as pd
import datetime as dt
import numpy as np 
import seaborn as sn
import matplotlib.pyplot as plt 


def parse_cols_basic():
    '''
    Combines all of the file data and lists the amount of citations per day
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
        counted_df = date_count(df)
        con_list.append(counted_df)
    for f in read_list_norm:
        df = pd.read_csv('python_read_files/' + f) # make sure to change this to the correct python read path
        counted_df = date_count(df)
        con_list.append(counted_df)
    output_df = pd.concat(con_list)
    return output_df


def date_count(a_df):
    '''
    Returns a dataframe consisting of the date and number of parking citations.
    Helper function for parse_cols_basic
    '''
    date_dict = {}
    output_DF = pd.DataFrame()
    dates = a_df['date_issue'].to_list()
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
    Takes input of parse_cols_basic() 
    '''
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
    Takes input of parse_cols_month(df)
    '''
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


def parse_cols_quarters(df):
    '''
    Combines all of the month's parking citations.
    Takes input of parse_cols_basic() 
    '''
    q = -1
    y = -1
    sum_count = 0
    q_in_same_y = []  
    output_DF = pd.DataFrame()
    for date in df.index:  
        datee = dt.datetime.strptime(date, "%Y-%m")
        #print(month_to_quarter(datee.month))
        if q == -1 or y == -1:  # keep track of previous quarter and to compare with current loop data
            q = month_to_quarter(datee.month)
        if y == -1:  # keep track of previous quarter and to compare with current loop data
            y = datee.year
        if q == 4 and datee.year == 2023: # covers edge case on last iteration
            q_in_same_y.append(None)
            output_DF[str(2023)] = q_in_same_y
            break
        elif month_to_quarter(datee.month) == q: # if same quarter, add month tickets
            sum_count += df.loc[date, 'count']
        elif month_to_quarter(datee.month) != q and datee.year == y: # if different quarter but same year, start a new ticket count
            q_in_same_y.append(sum_count)
            sum_count = df.loc[date, 'count']
            q = -1
        else: # if new year, start a new column
            q_in_same_y.append(sum_count)
            #print(q_in_same_y)
            output_DF[str(y)] = q_in_same_y
            q = -1
            y = -1
            q_in_same_y = [] 
            #q_in_same_y.append(df.loc[date, 'count'])
            sum_count = df.loc[date, 'count']
    
    month_names = ['Winter', 'Spring', 'Summer', 'Fall']
    output_DF.index = month_names

    return output_DF


def month_to_quarter(m):
    if 1 <= m <= 3:
        return 1 # winter
    elif 4 <= m <= 6:
        return 2 # spring
    elif 7 <= m <= 9:
        return 3 # summer
    elif 10 <= m <= 12:
        return 4 # fall
    else:
        return None
    

def parse_cols_daily(month, df):
    '''
    Cuts out all data besides the ones listed for a particular month.
    Takes input of parse_cols_basic() 
    '''

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
    Takes input of parse_cols_daily(df)
    '''
    y = -1
    d_in_same_y = []  
    output_DF = pd.DataFrame()
    month = 0
    for date in df.index:
        datee = dt.datetime.strptime(date, "%Y-%m-%d")   
        month = datee.month
        print(datee.year)
        if y == -1:
            y = datee.year
        if datee.year == y:
            #print(df.loc[date, 'count'])
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
    

pcb = parse_cols_basic()
pcm = parse_cols_month(pcb)
pcy = parse_cols_year(pcm)
pcq = parse_cols_quarters(pcm)
pcd = parse_cols_daily(12,pcb)
print(pcd)
pcd2 = parse_cols_daily2(pcd)
print(pcd2)
#print(pcq)
#print(pcy)

data_m = pcy.to_numpy()
data_q = pcq.to_numpy()
data_d2 = pcd2.to_numpy()


x_axis_labels = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
y_axis_labels_12 = ['January', 'February','March','April','May','June','July','August','September',
                    'October','November','December']
y_axis_lables_31 = list(range(1,32))
count = 0
for i in y_axis_lables_31:
    y_axis_lables_31[count] = "Day: " + str(i)
    count += 1

# plotting the heatmap 
cmap = sn.cm.rocket_r
hm = sn.heatmap(data_m, xticklabels=x_axis_labels, yticklabels=y_axis_labels_12, cmap = cmap) 
# displaying the plotted heatmap 
plt.show()

# plotting the heatmap 
hq = sn.heatmap(data=data_d2, xticklabels=x_axis_labels, yticklabels=y_axis_lables_31, cmap=cmap) 
# displaying the plotted heatmap 
#print(data_d2)
plt.show()