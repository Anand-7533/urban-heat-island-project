:

🌆 Urban Heat Island Detection & Visualization Dashboard
A data-driven web application to detect and visualize Urban Heat Island (UHI) effects in Chennai using geospatial temperature data and environmental indicators like NDVI, albedo, and impervious surfaces.

📌 Project Overview
Urban areas often experience significantly higher temperatures than surrounding regions—a phenomenon known as the Urban Heat Island effect. This project uses geospatial data and environmental metrics to:

Detect and visualize UHI zones.
Classify temperature severity.
Correlate land characteristics (NDVI, albedo, etc.) with surface temperature.
Provide real-time interactive visualizations via a Streamlit dashboard.

🧠 Problem Statement

“To identify, analyze, and visualize Urban Heat Island hotspots using land surface temperature and related geospatial factors, enabling smarter urban planning and climate resilience strategies.”

💡 Proposed Solution

Collect and analyze LST data from areas
Predict UHI intensity using ML or threshold logic.
Display heat zones and weather patterns using Folium, GeoPandas, and Streamlit.

🏗️ Project Architecture

Raw CSV & GeoData ➡️ Data Preprocessing ➡️ Temperature Classification ➡️ GeoJSON Layer Creation ➡️ Folium Map + Streamlit Dashboard

🛠️ Tech Stack

Category	Tools & Libraries
Language	Python
Geospatial	GeoPandas, Folium, Shapely
Visualization	Plotly, Streamlit, HTML/JS
Data Handling	Pandas, NumPy
UI & Dashboard	Streamlit, CSS (custom styles)

🚀 How to Run
Install dependencies:

pip install pandas geopandas folium streamlit plotly
Run the Streamlit dashboard:

streamlit run uhi_stream.py
Folder Structure:

urban_heat_island_project/
│
├── data1/                    # CSV files (e.g., temperature_data.csv)
├── output/                   # Generated GeoJSON & HTML Map
├── uhi_model.py              # Data processing & GeoJSON creation
├── uhi_map.py                # Folium map generation
├── uhi_stream.py             # Streamlit dashboard app
└── assets/                   # Background images & logos

📊 Features

Interactive temperature-based map with color-coded zones.
Weather condition emojis based on temperature.
Filterable charts for weather patterns.
Option to toggle dashboard background.

🌐 Real-Time Applications

City climate monitoring & urban planning.
Environmental risk assessment.
Community awareness & academic research.
Integration with IoT weather sensors.

✅ Conclusion

This project provides a scalable and intuitive system to visualize and understand Urban Heat Island patterns. With geospatial tools and data science, city planners can mitigate climate impact and make smarter development decisions.

