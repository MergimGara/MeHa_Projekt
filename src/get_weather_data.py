import os
import requests
import pandas as pd
from datetime import datetime

# Städte mit Koordinaten
cities = {
    "Berlin": (52.52, 13.405),
    "Paris": (48.8566, 2.3522),
    "Madrid": (40.4168, -3.7038),
    "Rome": (41.9028, 12.4964),
    "Vienna": (48.2082, 16.3738)
}

# Open-Meteo API URL
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Parameter vorbereiten
today = datetime.today().strftime("%Y-%m-%d")
params_base = {
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone": "Europe/Berlin",
    "start_date": today,
    "end_date": today
}

# Absoluten Pfad zum Projektverzeichnis ermitteln
project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, "../data")  # Ordner "data" im Projektverzeichnis

# Ordner erstellen
os.makedirs(data_dir, exist_ok=True)

# Daten abfragen
all_data = []

for city, (lat, lon) in cities.items():
    params = params_base.copy()
    params["latitude"] = lat
    params["longitude"] = lon

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        weather = response.json()
        times = weather["hourly"]["time"]
        temps = weather["hourly"]["temperature_2m"]
        humidity = weather["hourly"]["relative_humidity_2m"]

        for i in range(len(times)):
            all_data.append({
                "city": city,
                "datetime": times[i],
                "temperature": temps[i],
                "humidity": humidity[i]
            })
    else:
        print(f"Fehler bei {city}: {response.status_code}")

# Speichern als CSV
df = pd.DataFrame(all_data)
df.to_csv(os.path.join(data_dir, "weather_data_today.csv"), index=False)
print(f"✅ Wetterdaten gespeichert in {os.path.join(data_dir, 'weather_data_today.csv')}")
