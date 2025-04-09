import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import io

# 📁 Pfad zur CSV-Datei
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/weather_data_today.csv"))

# 📄 CSV einlesen
df = pd.read_csv(csv_path)
df['datetime'] = pd.to_datetime(df['datetime'])

# 🧱 Streamlit UI
st.title("🌤️ Wetterdaten europäischer Städte")

st.markdown("""
Diese Web-App zeigt Temperatur- und Luftfeuchtigkeitsdaten, die über die Open-Meteo API erfasst wurden.
""")

# 📌 Stadt-Auswahl
cities = df['city'].unique()
selected_cities = st.multiselect("Städte auswählen", options=cities, default=list(cities))

# 🔍 Gefilterte Daten
filtered = df[df['city'].isin(selected_cities)]

# ⏱️ Uhrzeit-Filter
st.subheader("⏰ Zeitfilter")
start_hour, end_hour = st.slider("Zeitraum auswählen (Stunden)", 0, 23, (6, 18))
filtered = filtered[
    (filtered['datetime'].dt.hour >= start_hour) &
    (filtered['datetime'].dt.hour <= end_hour)
]

# 🗂️ Tabs: Temperatur, Luftfeuchtigkeit, Statistik
tab1, tab2, tab3 = st.tabs(["🌡️ Temperatur", "💧 Luftfeuchtigkeit", "📊 Statistik / Korrelation"])

# 🌡️ Temperatur-Tab
with tab1:
    st.subheader("🌡️ Durchschnittstemperatur – Schnellübersicht")

    cols = st.columns(len(selected_cities))
    for i, city in enumerate(selected_cities):
        city_data = filtered[filtered["city"] == city]
        if not city_data.empty:
            avg_temp = city_data["temperature"].mean()
            cols[i].metric(label=f"{city}", value=f"{avg_temp:.1f} °C")

    st.subheader("📈 Temperaturverlauf")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered, x="datetime", y="temperature", hue="city", marker="o", ax=ax1)
    ax1.set_title("Temperaturverlauf")
    ax1.set_xlabel("Zeit")
    ax1.set_ylabel("Temperatur (°C)")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Download Temperatur-Plot
    img_buf1 = io.BytesIO()
    fig1.savefig(img_buf1, format="png")
    img_buf1.seek(0)
    st.download_button("📥 Temperaturdiagramm herunterladen", data=img_buf1, file_name="temperaturverlauf.png", mime="image/png")

    # Durchschnittstabelle
    avg_temp = filtered.groupby("city")["temperature"].mean().reset_index()
    avg_temp.columns = ["Stadt", "Durchschnittstemperatur (°C)"]
    st.dataframe(avg_temp.style.format({"Durchschnittstemperatur (°C)": "{:.2f}"}))

    # Tabelle Download
    csv_buf = avg_temp.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Temperaturtabelle herunterladen (CSV)", data=csv_buf, file_name="durchschnittstemperatur.csv", mime="text/csv")

# 💧 Luftfeuchtigkeit-Tab
with tab2:
    st.subheader("💧 Durchschnittliche Luftfeuchtigkeit")
    avg_humidity = filtered.groupby("city")["humidity"].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=avg_humidity, x="city", y="humidity", ax=ax2)
    ax2.set_title("Durchschnittliche Luftfeuchtigkeit")
    ax2.set_ylabel("Luftfeuchtigkeit (%)")
    st.pyplot(fig2)

    # Download Luftfeuchte-Plot
    img_buf2 = io.BytesIO()
    fig2.savefig(img_buf2, format="png")
    img_buf2.seek(0)
    st.download_button("📥 Luftfeuchtigkeitsdiagramm herunterladen", data=img_buf2, file_name="luftfeuchtigkeit.png", mime="image/png")

with tab3:
    st.subheader("📈 Korrelation: Temperatur vs. Luftfeuchtigkeit")

    if not filtered.empty:
        # Pearson-Korrelation berechnen
        from scipy.stats import pearsonr
        correlation, p_value = pearsonr(filtered["temperature"], filtered["humidity"])
        r_squared = correlation**2

        # Statistik anzeigen
        st.markdown(f"""
        **📊 Pearson-Korrelation:** {correlation:.3f}  
        **📐 R² (Bestimmtheitsmaß):** {r_squared:.3f}  
        **📉 p-Wert:** {p_value:.4f}  
        {"✅ Signifikant (p < 0.05)" if p_value < 0.05 else "❌ Nicht signifikant"}
        """)

        # Scatterplot mit Regressionslinie
        fig3 = sns.lmplot(
            data=filtered,
            x="temperature",
            y="humidity",
            hue="city",
            height=6,
            aspect=1.5,
            scatter_kws={"s": 40, "alpha": 0.6},
            line_kws={"color": "black", "linewidth": 1}
        )
        st.pyplot(fig3)

    else:
        st.info("Keine Daten für gewählten Zeitraum/Städte.")
