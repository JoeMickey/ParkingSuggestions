import pandas as pd

# read and concate the csv files
t = 1
for year in range(2012, 2024):
    for part in range(1,3):
        if year == 2012 and part == 1:
            df = pd.read_csv(f'./DataSource/parking_citations_{year}_part{part}_datasd.csv')
        else:
            df = pd.concat([df, pd.read_csv(f'./DataSource/parking_citations_{year}_part{part}_datasd.csv')], axis=0, ignore_index=True)

df.to_csv('database.csv', index=False)