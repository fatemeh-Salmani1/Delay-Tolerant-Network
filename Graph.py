import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
csv_file = "3_IncontactTimes.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

# Extract data from the DataFrame
bus_ids = df["Bus Id"][:50]
incontact_times = df["Incontact_Time"][:50]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(bus_ids, incontact_times, color='green')
plt.xlabel("Bus Id")
plt.ylabel("Incontact Time")
plt.title("Incontact Time for Different Buses")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the graph as an image file
output_file = "graph.png"  # Specify the desired output file name and format
plt.savefig(output_file)

# Optionally, you can also display a message indicating that the graph was saved
print(f"Graph saved as {output_file}")
