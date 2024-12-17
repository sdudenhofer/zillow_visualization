import pandas as pd
from datetime import datetime

pd.options.display.float_format = '{:.2f}'.format

data = pd.read_csv('Data/city_data.csv')
df = pd.DataFrame(data)

new_df = pd.DataFrame()
for value in df.columns:
    if '20' in value:
        new_value = datetime.strptime(value, '%Y-%m-%d').strftime('%Y-%m')
        df.rename(columns={value: new_value}, inplace=True)
        new_df['RegionID'] = df['RegionID']
        new_df['Year'] = datetime.strptime(new_value, '%Y-%m').strftime('%Y')
        new_df['Month'] = datetime.strptime(new_value, '%Y-%m').strftime('%m')
        new_df['Price'] = df[new_value]

print(new_df)
            