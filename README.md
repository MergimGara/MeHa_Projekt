# 🌤️ Wetteranalyse europäischer Städte – Scientific Programming FS2025

## 📌 Projektübersicht

Im Rahmen des Moduls *Scientific Programming* (FS2025) haben wir eine komplette Analyse- und Visualisierungs-Pipeline für Wetterdaten entwickelt.  
Die Daten werden über die **Open-Meteo API** in Echtzeit abgefragt, verarbeitet, analysiert und sowohl im Notebook als auch in einer interaktiven **Web-App** dargestellt.

Ziel: Temperatur- und Luftfeuchtigkeitsverläufe mehrerer Städte vergleichen und statistisch untersuchen.

---

## 🧪 Verwendete Technologien

- **Python 3.11**
- pandas
- matplotlib
- seaborn
- requests
- sqlite3
- streamlit
- Ollama (Lokal)
- python-dotenv

---

## 🚀 Projekt starten

### 🔹 Wetterdaten abrufen
```bash
python src/get_weather_data.py
```

### 🔹 Wetterdaten in SQLite speichern
```bash
python src/store_to_db.py
```

### 🔹 (Optional) GPT-Analyse via Ollama (Lokal)
```bash
python src/llm_summary.py
```

### 🔹 Analyse im Notebook öffnen
```bash
notebooks/weather_analysis.ipynb
```

### 🔹 Web-App starten
```bash
streamlit run app/streamlit_app.py
```

---

## 📁 Projektstruktur

```
MeHa_project/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── weather_data_today.csv
│   └── weather_data.db
├── notebooks/
│   └── weather_analysis.ipynb
├── src/
│   ├── get_weather_data.py
│   ├── store_to_db.py
│   └── llm_summary.py
├── .env               ← nicht mit abgeben!
├── requirements.txt
├── README.md
├── presentation_group_XX.pdf
└── videopresentation_group_XX.mp4
```

---

## ✅ Erfüllte Anforderungen

| Anforderung                            | Erfüllt |
|----------------------------------------|---------|
| Reale Wetterdaten (API)                | ✅ |
| Datenverarbeitung mit pandas           | ✅ |
| Python built-ins (Listen, Dicts etc.)  | ✅ |
| Schleifen & Bedingungen                | ✅ |
| Statistik mit p-Wert                   | ✅ |
| Visualisierung mit Plots               | ✅ |
| SQL & Datenbank                        | ✅ |
| LLM (GPT-Analyse, optional)            | ✅ |
| Streamlit Web-App                      | ✅ |
| ZIP-Abgabe + Präsentation              | ✅ |

---

## 🎁 Bonuspunkte (abgedeckt)

- ✅ Kreative Umsetzung mit Exportfunktionen
- ✅ Datenbankauswertung mit SQL
- ✅ LLM-Analyse integriert (Nur Lokal)
- ✅ Web-App zur Datenpräsentation

---

## 👥 Team

**Gruppe 25 – FS2025**  
**Teilnehmer:**
- Mergim Gara  
- Hasan Mahmuljin  

**Dozent:** Dr. Mario Gellrich

---

## 📝 Hinweise

- Alle Screenshots und Codeschnipsel zur Punktebegründung befinden sich im Anhang der PDF-Präsentation.
