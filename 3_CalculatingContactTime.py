import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from tqdm import tqdm

# Read the dataset with contact times
data_with_contact = pd.read_csv('2_CheckContacting.csv')  # Replace with the actual filename

# Choose the random bus ID for which you want to calculate in-contact times
random_bus_id = 'A412730'  # Replace with your chosen random bus ID

# Get a list of unique bus IDs in the dataset
all_bus_ids = data_with_contact['Bus Id'].unique()

# Create a dictionary to store in-contact times for each bus
incontact_times = {}

# Calculate in-contact times for each bus
for bus_id in tqdm(all_bus_ids, desc="Calculating in-contact times"):
    if bus_id != random_bus_id:
        incontact_time = data_with_contact[data_with_contact['Bus Id'] == bus_id]['Checking_Incontact'].sum()
        incontact_times[bus_id] = incontact_time

# Create a new DataFrame to store in-contact times
incontact_df = pd.DataFrame(list(incontact_times.items()), columns=['Bus Id', 'Incontact_Time'])

# Save the in-contact times to a new CSV file
incontact_df.to_csv('3_IncontactTimes.csv', index=False)  # Replace with desired filename
