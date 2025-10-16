import pandas as pd
import sqlalchemy
from dbcred import alchemycred

weather = pd.read_csv('open-meteo.csv')
weather = weather.rename(columns={'time': 'date'})
sales = pd.read_csv('sales_data.csv')

weather["date"] = pd.to_datetime(weather["date"], format="%m/%d/%y")

print(weather)
engine = sqlalchemy.create_engine(alchemycred)

weather.to_sql('weather', engine, if_exists='replace')
sales.to_sql('sales', engine, if_exists='replace')

query = " SELECT * FROM weather"
df = pd.read_sql_query(query, engine)
print(df)

query = " SELECT * FROM sales"
df = pd.read_sql_query(query, engine)
print(df)

# MySQL not having FULL OUTER JOIN is a form of terrorism

query = '''
        CREATE OR REPLACE VIEW sales_plus_weather AS
        SELECT COALESCE(s.date, w.date) AS date,
        s.weekday,s.sales,w.precipitation_sum,w.sunshine_duration,w.temperature_2m_max,
        w.temperature_2m_mean,w.temperature_2m_min,w.wind_direction_10m_dominant,
        w.wind_speed_10m_max,w.sunrise,w.sunset,w.daylight_duration,w.cloud_cover_mean,
        w.cloud_cover_max,w.cloud_cover_min,w.relative_humidity_2m_mean,w.snowfall_sum,
        w.rain_sum,w.precipitation_hours
        
        FROM sales AS s
        LEFT JOIN weather AS w
        ON s.date = w.date
        
        UNION
        SELECT COALESCE(s.date, w.date) AS date,
        s.weekday,s.sales,w.precipitation_sum,w.sunshine_duration,w.temperature_2m_max,
        w.temperature_2m_mean,w.temperature_2m_min,w.wind_direction_10m_dominant,
        w.wind_speed_10m_max,w.sunrise,w.sunset,w.daylight_duration,w.cloud_cover_mean,
        w.cloud_cover_max,w.cloud_cover_min,w.relative_humidity_2m_mean,w.snowfall_sum,
        w.rain_sum,w.precipitation_hours
        
        FROM sales AS s
        RIGHT JOIN weather AS w
        ON s.date = w.date;'''
df = pd.read_sql_query(query, engine)
print(df)
df.to_csv('sales_plus_weather.csv', index=False)

query = "SELECT * FROM sales_plus_weather"
df = pd.read_sql_query(query, engine)
print(df)
df.to_csv('sales_plus_weather.csv', index=False)

