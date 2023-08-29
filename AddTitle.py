


import csv

text_file_path = '2014-10-30.txt'
csv_file_path = '2014-10-30.csv'
delimiter = ','  
header_row = ['Date', 'Hour', 'Bus Id', 'Line', 'Latitude',
              'Longitude', 'Velocity']  

with open(text_file_path, 'r') as text_file:
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header_row)  # Write the header row
        for line in text_file:
            values = line.strip().split(delimiter)
            writer.writerow(values)
