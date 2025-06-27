import folium
import geopandas as gpd
import pandas as pd

# Load GeoJSON file
gdf = gpd.read_file('D:/urban_heat_island_project/output/uhi_predictions.geojson')

# Load CSV with temperature and weather condition
df_weather = pd.read_csv('D:/urban_heat_island_project/data1/temperature_data.csv')

# Weather icons mapping
icons = {
    'Clear': '☀️',
    'Clouds': '☁️',
    'Rain': '🌧️',
    'Thunderstorm': '⛈️',
    'Drizzle': '🌦️',
    'Snow': '❄️',
    'Mist': '🌫️'
}

# Map Center
lat_center = gdf.geometry.y.mean()
lon_center = gdf.geometry.x.mean()

# Color function for temperature
def get_color(temp):
    if temp > 40:
        return '#800026'
    elif temp > 38:
        return '#BD0026'
    elif temp > 36:
        return '#E31A1C'
    elif temp > 34:
        return '#FC4E2A'
    elif temp > 32:
        return '#FD8D3C'
    elif temp > 30:
        return '#FEB24C'
    else:
        return '#FFEDA0'

# Create map
m = folium.Map(location=[lat_center, lon_center], zoom_start=12)

# Add UHI prediction layer
folium.GeoJson(
    gdf,
    name='Urban Heat Zones',
    style_function=lambda feature: {
        'fillColor': get_color(feature['properties']['predicted_temp']),
        'color': 'black',
        'weight': 0.3,
        'fillOpacity': 0.7,
    },
    tooltip=folium.GeoJsonTooltip(fields=['predicted_temp'], aliases=['Predicted Temp (°C):'])
).add_to(m)

# Add weather condition icons from CSV
for _, row in df_weather.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    condition = row.get('weather_condition', 'Clear')
    icon = icons.get(condition, '🌈')
    temp = row['land_surface_temp']

    popup = f"{icon} {condition} ({temp}°C)"
    folium.Marker(
        location=[lat, lon],
        popup=popup,
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# Save the map
m.save('D:/urban_heat_island_project/output/uhi_map1.html')
print("✅ Map generated using CSV weather data!")
