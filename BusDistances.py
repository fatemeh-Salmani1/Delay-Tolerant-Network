import pandas as pd
import numpy as np
from geopy.distance import geodesic

# Load the dataset
data = pd.read_csv('1-TestPositionSpeed30S.csv')

# Convert the 'Timestamp', 'Latitude', and 'Longitude' columns to datetime and float
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Latitude'] = data['Latitude'].astype(float)
data['Longitude'] = data['Longitude'].astype(float)

# Get unique timestamps
timestamps = data['Timestamp'].unique()

# Create an empty list to store the results
bus_distances = []

# Counter for row conversion...For showing the process
row_count = 0

# Iterate through each unique timestamp
for timestamp in timestamps:
    # Get the data for the current timestamp
    timestamp_data = data[data['Timestamp'] == timestamp]
    
    # Iterate through each bus in the current timestamp
    for _, row in timestamp_data.iterrows():
        current_bus_id = row['Bus Id']
        current_latitude = row['Latitude']
        current_longitude = row['Longitude']
        
        # Calculate the distance to every other bus
        for _, other_row in timestamp_data.iterrows():
            other_bus_id = other_row['Bus Id']
            other_latitude = other_row['Latitude']
            other_longitude = other_row['Longitude']
            
            # Calculate the distance between the current bus and the other bus
            distance = geodesic((current_latitude, current_longitude), (other_latitude, other_longitude)).meters
            
            # Append the distance to the list of results
            bus_distances.append({
                'Timestamp': timestamp,
                'Bus Id 1': current_bus_id,
                'Bus Id 2': other_bus_id,
                'Distance (m)': distance
            })
            
            #For showing the process
            row_count += 1
            # Print the row count during execution
            print("Rows processed:", row_count, end="\r")

# Create a new dataframe from the list of bus distances
distances_data = pd.DataFrame(bus_distances)

# Save the distances dataset to a CSV file
distances_data.to_csv('BusDistances.csv', index=False)

# Print the final row count..For showing the process
print("Number of rows processed:", row_count)
