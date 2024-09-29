import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql://seth:G0thl0rd1@localhost:5432/city_data')


data = pd.read_csv('Data/city_data.csv')
df = pd.DataFrame(data)
# TODO transform data so each entry has only one date
df.to_sql(name='city_data', con=engine)
