# main.py

import pandas as pd
import time_series_analysis

def read_dataset():
    '''
    :return: DataFrame of our dataset
    '''
    df = pd.read_csv('database.csv')
    return df


if __name__ == "__main__":

    df = read_dataset()

    # population regression analysis (Exclude 2020)
    population_p_value = time_series_analysis.population_correlation(df, include_2020=False, visualization=True)

    # parking meters analysis
    parking_meters_p_value = time_series_analysis.parking_meters_correlation(df, visualization = True)

    # existing parking meters and parking ticket frequency changes scatter graph
    time_series_analysis.parking_meters_scatter_plot(df)

    # heatmap for October, November. December and for monthly of past decade
    time_series_analysis.time_heatmap_monthly(df, month = 10)
    time_series_analysis.time_heatmap_monthly(df, month = 11)
    time_series_analysis.time_heatmap_monthly(df,month = 12)
    time_series_analysis.time_heatmap_yearly(df)

    # seasonal decompose
    seasonal_decomposition = time_series_analysis.seasonal_decompose(df, visualization=True)
