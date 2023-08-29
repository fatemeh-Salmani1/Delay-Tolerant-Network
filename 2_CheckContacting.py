import pandas as pd
import random
from math import radians, sin, cos, sqrt, atan2
from tqdm import tqdm

# Read the dataset with distances
data_with_distances = pd.read_csv('1_DistanceCalculation.csv')  # Replace with the actual filename

# Function to calculate contact time
def calculate_contact_time(distance, velocity):
    if distance < 250 and velocity > 0:  # Considered in contact if distance < 250 and velocity > 0
        return 1  # Assuming 1 unit of time for contact
    return 0

# Calculate contact times and add them to the dataset as a new column
contact_times = []
for index, row in tqdm(data_with_distances.iterrows(), total=len(data_with_distances), desc="Calculating contact times"):
    contact_time = calculate_contact_time(row['Distance_to_selected_bus'], row['Velocity'])
    contact_times.append(contact_time)

# Add contact times to the dataset as a new column
data_with_distances['Checking_Incontact'] = contact_times

# Save the dataset with contact times
data_with_distances.to_csv('2_CheckContacting.csv', index=False)  # Replace with desired filename
