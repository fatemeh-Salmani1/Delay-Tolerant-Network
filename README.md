# Bus Data Analysis and Communication in Rio de Janeiro
## Overview

This project focuses on analyzing bus data in Rio de Janeiro, Brazil, with the goal of understanding the interactions and communication between buses on the road. The primary objectives are to reduce the granularity of the data, calculate the distances between buses, and determine when buses come into contact with each other within a specified range.
## Data

#### The dataset used in this project contains detailed information about buses, including:

    Date
    Hour
    Bus ID
    Line
    Latitude
    Longitude
    Velocity

The original dataset records data for each minute throughout the entire day, which is too fine-grained for our analysis. We will initially reduce this data to 30-second intervals and then further down to 10-second intervals to make it more manageable.
## Data Processing

    Data Reduction: We start by reducing the time intervals in the dataset from one minute to 30 seconds, and subsequently down to 10 seconds. This will provide a more precise representation of bus movements.

    Distance Calculation: With the reduced dataset, we calculate the distances between all buses. This step is crucial for understanding the spatial relationships between buses on the road.

    Contact Detection: We define a communication range, which acts as a radius around each bus. We then determine when two buses come into contact within this range. Contact detection helps us understand when and how buses interact with each other.

## Output

The main output of this project is a new dataset that includes information about the duration of contact between buses for each unique bus ID. This dataset can provide valuable insights into bus communication patterns and interactions on the road.
## Usage

#### To use this project, follow these steps:

    Data Preparation: Make sure you have the original bus dataset ready.

    Data Reduction: Use the provided scripts to reduce the data to 30-second intervals and then to 10-second intervals.

    Distance Calculation: Calculate the distances between buses using the provided scripts.

    Contact Detection: Define the communication range and run the contact detection script to find out when and how buses come into contact.

    Result Analysis: Analyze the generated dataset to gain insights into bus interactions and communication patterns.

## Dependencies

    Python 3.x
    Pandas
    Math
    Tqdm
    Matplotlib
    Other dependencies as specified in the scripts

## Contributing

Contributions to this project are welcome. Please open an issue or submit a pull request with your suggestions or improvements.
## License

This project is licensed under the MIT License.


