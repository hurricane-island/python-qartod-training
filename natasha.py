# This is an introduction to python
# We are typing in buoy variables.
Column_1 = "Temperature"
Column_2 = "Salinity"
Column_3 = "ODO"  # Optical Disolced Oxygen

# This is a list which orders the collection of items
buoyMMA_parameters_list = [Column_1, Column_2, Column_3]

buoyMMA_parameters_list.remove(Column_2)

buoyMMA_parameters_list.insert(1, Column_2)

print("The parameters we are measuring are:", buoyMMA_parameters_list)

buoyMMA_parameters_dict = {
    "Temperature": Column_1,
    "Salinity": Column_2,
    "Optical_Disolved_Oxygen": Column_3,
}

print(f"The parameters we are measureing are: {buoyMMA_parameters_dict}")

# Defining sensor limits
SENSOR_MAX = 50  # units: RFU, this is an integer
SENSOR_MIN = 0.0  # RFU, this is a float because it has a decimal point
USER_MAX = 35  # RFU, integer
USER_MIN = 25.0  # RFU, float

salinity_ex_data = [
    28.4,
    39.7,
    26.1,
    30.8,
    25.6,
    34.9,
    51.7,
    31.0,
    29.5,
    32.2,
]  # This is a list of example salinity

"""
We are going to use a for loop to iterate through the salinity data and check if the values are within the sensor and user limits.
We will use if-else statements to check the values and print a message if they are outside the sensor and user limits. 
"""


for value in salinity_ex_data:
    if value > SENSOR_MAX or value < SENSOR_MIN:
        print(f"Fail sensor and user limit: {value}")
    elif value > USER_MAX or value < USER_MIN:
        print(f"Fail user limit: {value}")
    else:
        print("pass")

# built in functions
# len() will tell you the length of the list
# print() print in output
# type() will tell you the data type

# import the datetime modules from the library
from datetime import datetime, timezone

def time_format():
    response = datetime.now()
    return print(response)
time_format()


def time_format():
    response = datetime.now().isoformat()
    return print (response)
time_format()