import polars as pl
import datetime as dt

data = pl.read_csv('Data/city_data.csv')
df = pl.DataFrame(data)

df_2000 = pl.DataFrame()
for value in df.columns:
    if '2000' in value:
        dictionary = []
        if value != dictionary:
            new_date = dt.datetime.strptime(value, '%Y-%m-%d').strftime('%Y-%m')
            df_2000 = df[['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName', 'State', 'Metro', 'CountyName', value]]
        dictionary.append(value)

print(df_2000)

