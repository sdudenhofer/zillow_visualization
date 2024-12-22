import polars as pl
import datetime as de

data = pl.read_csv('Data/city_data.csv')
df = pl.DataFrame(data)

for value in df.columns:
    if type(value) is de.datetime:
        print(value)
