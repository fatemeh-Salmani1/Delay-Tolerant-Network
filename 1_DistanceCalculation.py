import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from tqdm import tqdm

# Read the dataset
data = pd.read_csv('0_2014-10-01.csv')  # Replace 'your_dataset.csv' with the actual filename

# Select the bus with a specific ID
selected_bus_id = "A412730"
selected_bus_row = data[data['Bus Id'] == selected_bus_id].iloc[0]

# Extract the latitude and longitude of the selected bus
selected_bus_lat = selected_bus_row['Latitude']
selected_bus_lon = selected_bus_row['Longitude']

# Haversine formula to calculate distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's radius in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Calculate distances between the selected bus and all other buses
distances = []
for index, row in tqdm(data.iterrows(), total=len(data), desc="Calculating distances"):
    distance = haversine(selected_bus_lat, selected_bus_lon, row['Latitude'], row['Longitude'])
    distances.append(distance)

# Add distances to the dataset as a new column
data['Distance_to_selected_bus'] = distances

# Save the updated dataset with distances
data.to_csv('1_DistanceCalculation.csv', index=False)  # Replace with desired filename
