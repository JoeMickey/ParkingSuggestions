# ECE143Project
Repository for ECE 143 Project Fall 2023

Project Summary
With the dataset of Parking Citations in the San Diego area published by the City Treasurer, along with the population data and the parking meters data, we conducted a series of analysis including Statistical Exploration, Time-Series Heat Map Visualization, Seasonal Decomposation, Linear Regression, Geospatial Heat Map Visualization and Interactive Map Folium to explore the characteristics of the parking tickets from the perspectives of time and space.  

Our research conclusion shows when and where more parking tickets can be found, and explains the factors that may contribute to such characteristic. Moreover, we provide some tips for parking when it’s almost impossible to park in the parking lot.

we also developed a small client-side web application that will tell a user if they are prone to parking tickets based on the street name and the time, with the help of Google Map API. We will keep exploring the integration of the web application and our algorithsm to make it ready for publish.

Dataset:
Resource: https://data.sandiego.gov/datasets/parking-citations/
The dataset issued by City Treasurer contains Parking Citations data since 2012, published in a half-year frequency, with eight factors including the date, location, reason, issue department and fine amount of the tickets. 

Resource: https://data.sandiego.gov/datasets/parking-meters-locations/
The dataset issued by City Treasurer contains Parking Meters data since 2018 in a daily frequency, with ten factors including the date, location, latitude and longitude of the parking meters. 

Resource: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html
The dataset issued by US Census Bureau contains population statistics in San Diego in a yearly frequency.

Files Introduction
datasets_merge.py: It merges the datasets that are originally published in a hal-year frequency.
Data Analysis.ipynb: It generates the series of visualizations from the statistical exploration.
date_count_heatmap.py: It generates the Time-Series Heatmap of the parking tickets.
Correlation Exploration.ipynb: It generates the seasonal decomposing result of the time-series, as well as correlations between parking tickets and population and parking places.
Parking Tickets GeoSpatial.ipynb: It generates the interactive map of the parking tickets' statistical characteristic.
geospatial_analaysis_parking.html: The interactive map generated from Parking Tickets GeoSpatial.ipynb.



