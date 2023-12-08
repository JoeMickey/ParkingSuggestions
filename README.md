# A San Diego Parking Tickets Data Analysis and GeoSpatial Visualization

With the dataset of Parking Citations in the San Diego area published by the City Treasurer, we conduct a series of analysis including Linear Regression, Geospatial Heat Map Visualization to explore the characteristics of the parking tickets from the perspectives of time and space.  
Our research conclusion shows and explains why there are times and places where more parking tickets can be found, so that we provide some tips for parking when it's almost impossible to park in the parking lot. Moreover, we develop a small client-side web application that will tell a user if they are prone to parking tickets based on the street name and the time, with the help of Google Map API.

Datasets
1. Parking Tickets in San Diego Between 2012-2023
2. Population in Cities of San Diego Between 2012-2022
3. Parking Meters in San Diego Between 2018-2023
4. Parking Lots in San Diego Between 2016-2023


# File Structure

- `Datasets/`: This folder contains all the csv files of Datasets
    - `Parking Ticket Databases/`: original datasets of Parking Tickets in San Diego Between 2012-2023
    - `population_cities_2010_2022.csv`: original dataset of Population in Cities of San Diego Between 2012-2022
    - `parking_meters_loc_datasd.csv`: original dataset of Parking Meters in San Diego Between 2018-2023
    - `park_lots_loc_datasd.csv`: original dataset of Parking Lots in San Diego Between 2016-2023

- `Web App/`: This folder contains files for Website Application
    - `build/`: files for website development
    - `future_scope.py`: codes for parking suggestion generation 
    - `suggestion_model.pkl`: model for suggestion generation
    - `OneHotEncoders.pkl`: one-hot encoders for suggestion generation
 
- `ECE143-Group10_Final Presentation.pdf`: final presentation slides for our project
- `time_series_analysis.py`: functions used for time series analysis including correlation exploration, regression, seasonal decompose, heatmap


# Time_Series_Analysis
Visualizes the number of parking citations using heatmaps over the course of 2012 - 2023. Creates plots of all months, all days in October, November, and December. Creates time series analyses and describes daily, weekly, and seasonal trends

- `Functions/`:
    - `time_series_analysis.main()/`:
        - `Desc.`: import datasets as DataFrame
    - `time_series_analysis.date_reframe(df, date_column, daily = False, monthly = False, yearly = False)/`:
        - `df`: original dataframe of databases
        - `date_column`: the column name of date
        - `daily`: if need daily count (bool)
        - `monthly`: if need monthly count (bool)
        - `yearly`: if need yearly count (bool)
        - `Desc.`: the periodic frequency of the tickets
    - `time_series_analysis.regression_visualization(model, x, y, category)/`:
        - `model`: the regression model
        - `x`: the original x variable
        - `y`: the original y variable
        - `category`: the required plot (population/parking meters)
        - `Desc.`: scattered points and linear ploting
    - `time_series_analysis.population_correlation(df, include_2020 = True, visualization = False)/`:
        - `df`: the original DataFrame
        - `include_2020`: if include the impact of pandamic (bool)
        - `visualization`: if show the visualization (bool)
        - `Desc.`: return P-Value of the regression for population and parking tickets correlation analysis
    - `time_series_analysis.parking_meters_correlation(df, visualization = False)/`:
        - `df`: the original DataFrame
        - `visualization`: if show the visualization (bool)
        - `Desc.`: return P-Value of the regression for parking meters and parking tickets correlation analysis
    - `time_series_analysis.parking_meters_scatter_plot(df)/`:
        - `df`: the original DataFrame
        - `Desc.`: for visualization of scattered points of parking meters and tickets
    - `time_series_analysis.lockdown(ds)/`:
        - `ds`: the date 
        - `Desc.`: return result (bool) for identification if the day is during lockdown
    - `time_series_analysis.seasonal_decompose(df, visualization = False)/`:
        - `df`: the original DataFrame 
        - `visualization`: if show the visualization (bool)
        - `Desc.`: for season decomposition analysis
    - `time_series_analysis.time_heatmap_yearly(df)/`:
        - `df`: the original DataFrame 
        - `Desc.`: plot heatmap for months
    - `time_series_analysis.time_heatmap_monthly(df, month)/`:
        - `df`: the original DataFrame 
        - `month`: month for heatmap
        - `Desc.`: plot heatmap for certain month
    - `time_series_analysis.parse_cols_month(df)`
        - `df`: sorted dataframe with parking citation data
        - `Desc.`: combines all of the month's parking citations, returns a dataframe object
    - `time_series_analysis.parse_cols_year(df)`
        - `df`: output dataframe of parse_cols_month(df)
        - `Desc.`: lists the parking citation count by month (rows) and by year (columns), returns a dataframe object
    - `time_series_analysis.parse_cols_daily(month, df)`
        - `df`: sorted dataframe with parking citation data
        - `month`: month to capture data from
        - `Desc.`: combines all of the month's parking citations, returns a dataframe object
    - `time_series_analysis.parse_cols_daily2(df)`
        - `df`: output dataframe of parse_cols_daily(df)
        - `Desc.`: lists the parking citation count by day (rows) and by year (columns), returns a dataframe object
    - `time_series_analysis.parse_cols_basic()`
        - `Desc.`: Combines all of the file data and lists the amount of citations per day in order. Make sure to                       change the read paths for the .csv files
    



# Usage
To display the SD map

1. run process_sd_visuals.ipynb

    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "sd_final.csv" is already in ./src

2. execute display_sd.ipynb from ./src which displays the data from sd_final.csv

end

To display the SF map

1. run process_sf_visuals.ipynb
        
    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "sf_final.csv" is already in ./src

2. execute display_sf.ipynb from ./src which displays the data from sf_final.csv

end

To display the NY map

1. run process_ny.ipynb
        
    i. doing so requires you to insert your own api key for routes and directions
    
    ii. doing so will also take a long time

    iii. the output "ny_final.csv" is already in ./src
    
2. execute display_ny.ipynb from ./src which displays the data from ny_final.csv

end

To display time series graphics

1. 'import time_series_analysis.py'

2. ensure that the dataframe with parking citation data has been created and is in order of time

3. call 'time_series_analysis.main(df)', where df is the dataframe consisting of parking citation data

end

# Installations

**Before running this project, please install the following Python libraries:**

- pandas
- numpy
- plotly
- requests
- tqdm
- folium
- seaborn
- matplotlib
- statsmodels
- prophet
- geopy

**These packages are built-in. No install needed:**

- sys
- ast
- time
- datetime
- collections
- pickle

**Versions used:**

- Python 3.11.1
- pandas 1.5.3
- numpy 1.24.1
- plotly 5.13.1
- requests 2.28.2
- tqdm 4.65.0
- folium 0.14.0
- seaborn 0.13.0
- matplotlib 3.8.2
- statsmodels 0.14.0
- prophet 1.1.5
- geopy 2.4.0

All of the dependencies can be installed in the terminal using the command:

```
pip install -r requirements.txt
```

# Preprocessing Datasets

## Preprocessing the San Diego Traffic Volumes Dataset

In this section, we will be preprocessing the San Diego traffic dataset. The raw dataset is located in `datasets/traffic_counts_datasd_v1.csv`. 

To preprocess this dataset, we will run the script `process_sd_data.py` that is located in the `src/` folder

1. Navigate to the src folder
```
cd src
```

2. In order to preprocess this dataset, we will run the `process_sd_data.py`. Make sure to also include the following flags:

    i. `--input_dir`: Specify the path to the raw dataset to be processed.

    ii. `--output_dir`: Specify the path to the new preprocessed dataset. Be sure to also include the csv file name.

    iii. `--log_start_streets`: Specify the path to the text file that contains incorrect starting street names.

    iv. `--log_end_streets`: Specify the path to the text file that contains the incorrect ending street names.

    v. `--get_invalid_streets` (Optional): Boolean flag. Set this flag to True to get the list of incorrect starting and ending street names. 

    **NOTES:** 
    
        a. The directory paths must be relative to the path from the `src/` folder since that is our current directory.
        
        b. Running the following proprocessing script can take about 1.5 hours since it calls the geocoding API which takes time to compute.

    Here is an example of how to run the code to preprocess the San Diego traffic dataset.

    ```
    python process_sd_data.py --input_dir ../datasets/traffic_counts_datasd_v1.csv --output_dir ../processed_datasets/sd_data_processed.csv --log_start_streets ../logs/start_roads_to_fix.txt --log_end_streets ../logs/end_roads_to_fix.txt
    ```
    
    The final preprocessed San Diego dataset will be located in the `processed_datasets` folder under the name `sd_data_preprocessed.csv`. 

## Preprocessing the San Francisco Traffic Counts Dataset

In this section, we will be preprocessing the San Francisco traffic dataset. The raw dataset is located in `datasets/sfmta_corridor_counts_2014-2018.csv`.

We will be using the same method we used to preprocess the San Diego dataset.

To preprocess this dataset, we will run the script `process_sf_data.py` that is located in the `src/` folder

1. Navigate to the src folder
```
cd src
```

2. In order to preprocess this dataset, we will run the `process_sd_data.py`. Make sure to also include the following flags:

    i. `--input_dir`: Specify the path to the raw dataset to be processed.

    ii. `--output_dir`: Specify the path to the new preprocessed dataset. Be sure to also include the csv file name.

    **NOTES:** 
    
        a. The directory paths must be relative to the path from the `src/` folder since that is our current directory.
        
        b. Running the following proprocessing script can take about 1.5 hours since it calls the geocoding API which takes time to compute.

    Here is an example of how to run the code to preprocess the San Francisco traffic dataset.

    ```
    python3 process_sf_data.py --input_dir ../datasets/sfmta_corridor_counts_2014-2018.csv --output_dir ../processed_datasets/sf_data_processed.csv
    ```
    
    The final preprocessed San Francisco dataset will be located in the `processed_datasets` folder under the name `sf_data_preprocessed.csv`. 


# References
**Data:**  
[San Diego Parking Citation Data](https://data.sandiego.gov/datasets/parking-citations/)   
[San Diego Parking Meters Data](https://data.sandiego.gov/datasets/parking-meters-locations/)  
[San Diego Parking Lots Data](https://data.sandiego.gov/datasets/park-locations/)  
[San Diego Population Data](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html)  



