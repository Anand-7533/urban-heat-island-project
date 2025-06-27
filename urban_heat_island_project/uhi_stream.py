import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import geopandas as gpd
import streamlit.components.v1 as components

# Set Streamlit config
st.set_page_config(layout="wide", page_title="UHI Dashboard")
st.title("🌆 Urban Heat Island Visualization Dashboard")

# Toggle for background
bg_toggle = st.sidebar.toggle("🎨 Toggle Background", value=True)

# Function to apply background
def set_background(image_file_path):
    with open(image_file_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply background only if toggle is ON
if bg_toggle:
    set_background("D:/urban_heat_island_project/assets/bg.jpg")

# ⚙️ Paths
CSV_PATH = "D:/urban_heat_island_project/data1/temperature_data.csv"
MAP_PATH = "D:/urban_heat_island_project/output/uhi_map1.html"
GEOJSON_PATH = "D:/urban_heat_island_project/output/uhi_predictions.geojson"

# 📄 Load Data
df = pd.read_csv(CSV_PATH)
gdf = gpd.read_file(GEOJSON_PATH)

# 🔍 Sidebar Filter
weather_options = ["All"] + sorted(df["weather_condition"].dropna().unique().tolist())
selected_weather = st.sidebar.selectbox("☁️ Filter by Weather Condition", weather_options)

# 📊 Filter DataFrame
filtered_df = df if selected_weather == "All" else df[df["weather_condition"] == selected_weather]

# 🗺️ Display Embedded HTML Map
st.subheader("🗺️ Urban Heat Island Map")
with open(MAP_PATH, "r", encoding="utf-8") as f:
    map_html = f.read()
components.html(map_html, height=600)

# 📈 Weather Frequency Chart
st.subheader("📊 Weather Condition Frequency")
weather_df = df["weather_condition"].value_counts().reset_index()
weather_df.columns = ["weather_condition", "count"]

weather_chart = px.bar(
    weather_df,
    x="weather_condition",
    y="count",
    labels={"weather_condition": "Weather", "count": "Count"},
    color="weather_condition",
    title="Weather Condition Frequency"
)
st.plotly_chart(weather_chart, use_container_width=True)

# 🧾 Show Data Table
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered_df, use_container_width=True)
