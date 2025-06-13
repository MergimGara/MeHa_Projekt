import sqlite3
import pandas as pd
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/weather_data.db"))

# Verbindung aufbauen
conn = sqlite3.connect(db_path)

# SQL-Abfrage mit MIN, MAX, AVG
query = """
SELECT 
    city,
    MIN(temperature) AS min_temp,
    MAX(temperature) AS max_temp,
    AVG(temperature) AS avg_temp
FROM weather
GROUP BY city
ORDER BY avg_temp DESC;
"""

df = pd.read_sql_query(query, conn)

print("🌡️ Temperaturstatistik je Stadt:")
print(df)

conn.close()
