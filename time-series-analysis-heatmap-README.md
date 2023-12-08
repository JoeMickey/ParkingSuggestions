# Time Series Heatmap

Visualizes the number of parking citations using heatmaps over the course of 2012 - 2023. Creates plots of all months, all days in October, November, and December.

It was found that the colder seasons (fall, winter) have less parking citations. Additionally, there were fewer parking citations on federal holidays and more citations during the weekday.

# Files

- `time_series_analysis.py/`: This file contains the code to create the above mentioned heatmaps

# Function

- `Callable Function`: date_count_heatmap.main(df)
    - `df`: dataframe object containing parking citations in sorted order from Jan 2012 to Oct 2023
    - `Desc.`: Parses data and creates four heatmaps

# Usage
To call the function inside another python file

1. 'import time_series_analysis.py'

2. ensure that the dataframe with parking citation data has been created and is in order of time

3. call 'time_series_analysis.main(df)', where df is the dataframe


# Installations

**Before running this project, please install the following Python libraries:**

- pandas
- datetime
- numpy
- seaborn
- matplotlib


# References
**Data:**  
[San Diego Parking Citation Data](https://data.sandiego.gov/datasets/parking-citations/)  
- `datasets used in dataframe/`: original datasets used in for input dataframe
    - `parking_citations_2012_part1_datasd.csv`: San Diego Ticket Citation List dataset (2012)
    - `parking_citations_2012_part2_datasd.csv`: San Diego Ticket Citation List dataset (2012)
    - `parking_citations_2013_part1_datasd.csv`: San Diego Ticket Citation List dataset (2013)
    - `parking_citations_2013_part2_datasd.csv`: San Diego Ticket Citation List dataset (2013)
    - `parking_citations_2014_part1_datasd.csv`: San Diego Ticket Citation List dataset (2014)
    - `parking_citations_2014_part2_datasd.csv`: San Diego Ticket Citation List dataset (2014)
    ...
    - `parking_citations_2023_part1_datasd.csv`: San Diego Ticket Citation List dataset (2023)
    - `parking_citations_2023_part2_datasd.csv`: San Diego Ticket Citation List dataset (2023)

