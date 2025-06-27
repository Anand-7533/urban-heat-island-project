# uhi_model.py

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Load temperature dataset
df = pd.read_csv('D:/urban_heat_island_project/data1/temperature_data.csv')


# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")

# Features and target
X = gdf[['NDVI', 'albedo', 'impervious_surface']]
y = gdf['land_surface_temp']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict all temperatures
gdf['predicted_temp'] = model.predict(X)

# Save GeoJSON with predicted temperatures
gdf[['latitude', 'longitude', 'predicted_temp', 'geometry']].to_file('D:/urban_heat_island_project/output/uhi_predictions.geojson', driver='GeoJSON')


# Plot the result
gdf.plot(column='predicted_temp', cmap='hot', legend=True, figsize=(10, 6))
plt.title("Predicted Urban Heat Island Zones")
plt.show()
