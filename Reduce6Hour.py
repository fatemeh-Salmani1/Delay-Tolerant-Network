import pandas as pd

# Load the dataset
data = pd.read_csv('2014-10-01.csv')

# Convert the 'Date' and 'Hour' columns to datetime
data['Timestamp'] = pd.to_datetime(data['Date'] + ' ' + data['Hour'])

# Sort the data by timestamp
data = data.sort_values('Timestamp')

# Define the time range to exclude (first 6 hours)
start_time = data['Timestamp'].min()
end_time = start_time + pd.Timedelta(hours=6)

# Filter the data to exclude the first 6 hours
filtered_data = data[data['Timestamp'] >= end_time]

# Save the filtered dataset to a new CSV file
filtered_data.to_csv('Reduce6Hour.csv', index=False)
