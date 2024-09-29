import pandas as pd

data = pd.read_csv('Data/city_data.csv')
df = pd.DataFrame(data)
print(df.head)
