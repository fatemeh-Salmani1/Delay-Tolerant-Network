# import pandas as pd

# # Load the dataset
# data = pd.read_csv('OneHourOfBigDataset.csv')

# # Convert the 'Date' and 'Hour' columns to datetime
# data['Timestamp'] = pd.to_datetime(data['Date'] + ' ' + data['Hour'])

# # Sort the data by timestamp
# data = data.sort_values('Timestamp')

# # Create an empty list to store the results
# bus_positions = []

# # Iterate through each row in the dataset
# for _, row in data.iterrows():
#     # Get the timestamp, latitude, longitude, and velocity
#     timestamp = row['Timestamp']
#     bus_id = row['Bus Id']
#     line = row['Line']
#     latitude = row['Latitude']
#     longitude = row['Longitude']
#     velocity = row['Velocity']
    
#     # Calculate the time intervals between 10-second intervals
#     time_intervals = pd.date_range(timestamp, periods=int(velocity*6), freq='10S')
    
#     # Calculate the speed for each time interval
#     speeds = [velocity] * len(time_intervals)
    
#     # Create a new row for each time interval
#     for interval, speed in zip(time_intervals, speeds):
#         bus_positions.append({
#             'Timestamp': interval,
#             'Bus Id': bus_id,
#             'Line': line,
#             'Latitude': latitude,
#             'Longitude': longitude,
#             'Speed': speed
#         })

# # Create a new dataframe from the list of bus positions
# new_data = pd.DataFrame(bus_positions)

# # Save the new dataset to a CSV file
# new_data.to_csv('3_TestOneHourOfBigDataset10S.csv', index=False)




import pandas as pd
from tqdm import tqdm
import time

# Open the input and output files
with open('2014-10-01.csv', 'r') as input_file, open('GenerateLocation&Speed10S.csv', 'w') as output_file:
    # Write the header to the output file
    output_file.write('Timestamp,Bus Id,Line,Latitude,Longitude,Speed\n')
    
    # Read the first line of the input file
    header = input_file.readline().strip().split(',')
    
    # Get the column indices
    date_index = header.index('Date')
    hour_index = header.index('Hour')
    bus_id_index = header.index('Bus Id')
    line_index = header.index('Line')
    latitude_index = header.index('Latitude')
    longitude_index = header.index('Longitude')
    velocity_index = header.index('Velocity')
    
    # Read the first line of data
    line = input_file.readline().strip().split(',')
    prev_timestamp = pd.to_datetime(line[date_index] + ' ' + line[hour_index])
    prev_latitude = float(line[latitude_index])
    prev_longitude = float(line[longitude_index])
    prev_velocity = float(line[velocity_index])
    
    # Process the remaining lines
    for line in tqdm(input_file, desc='Processing lines'):
        # Split the line into values
        line = line.strip().split(',')
        
        # Get the current timestamp, latitude, longitude, and velocity
        timestamp = pd.to_datetime(line[date_index] + ' ' + line[hour_index])
        latitude = float(line[latitude_index])
        longitude = float(line[longitude_index])
        velocity = float(line[velocity_index])
        
        # Calculate the time difference between the current and previous timestamp
        time_diff = (timestamp - prev_timestamp).total_seconds()
        
        # Calculate the number of intermediary positions to add
        if time_diff > 0:
            num_positions = int(time_diff / 10) + 5  
        else:
            num_positions = 0
        
        # Calculate the latitude and longitude increments
        if num_positions > 0:
            lat_increment = (latitude - prev_latitude) / num_positions
            lon_increment = (longitude - prev_longitude) / num_positions
        
            # Write the intermediary positions to the output file
            for i in range(1, num_positions+1):
                current_timestamp = prev_timestamp + pd.Timedelta(seconds=10*i)
                current_latitude = prev_latitude + lat_increment * i
                current_longitude = prev_longitude + lon_increment * i
                output_file.write(f'{current_timestamp},{line[bus_id_index]},{line[line_index]},'
                                  f'{current_latitude},{current_longitude},{prev_velocity}\n')
        
        # Update the previous values
        prev_timestamp = timestamp
        prev_latitude = latitude
        prev_longitude = longitude
        prev_velocity = velocity
