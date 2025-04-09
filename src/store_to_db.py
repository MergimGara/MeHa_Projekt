import os
import sqlite3
import pandas as pd

# Absoluten Pfad zum Projektverzeichnis ermitteln
project_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(project_dir, "../data/weather_data_today.csv")
db_file = os.path.join(project_dir, "../data/weather_data.db")

# CSV einlesen
if not os.path.exists(data_file):
    raise FileNotFoundError(f"Die Datei {data_file} wurde nicht gefunden. Stellen Sie sicher, dass sie existiert.")

df = pd.read_csv(data_file)

# Verbindung zur SQLite-Datenbank (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Tabelle anlegen (falls nicht existiert)
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    datetime TEXT,
    temperature REAL,
    humidity REAL
)
""")

# Daten einfügen
df.to_sql("weather", conn, if_exists="replace", index=False)

# Beispiel-Query: Durchschnittstemperatur je Stadt
result = pd.read_sql_query("""
SELECT city, AVG(temperature) as avg_temp
FROM weather
GROUP BY city
ORDER BY avg_temp DESC
""", conn)

print(result)

# Verbindung schließen
conn.close()
