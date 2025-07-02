# This is an introduction to Python. 
# In Python, the main data types are:
    # int, float, str, bool, list, tuple, set, dict

column_1 = 'Time' #This is defining the variable column_1 and assigning it to Time which is a string
column_2 = 'Temperature' #Strings are sequences of characters
column_3 = 'Conductivity' #Strings can be defined with single quotes
column_4 = "Salinity" #strings can also be defined with double quotes
column_5 = "Chlorophyll"
column_6 = "BGA_PE" #PE stands for phycoerythrin

#To store all these variables, we can use a list, tuple, or dictionary.

#This is a list, which is an ordered collection of items that can be changed at any point. 
buoy_parameters_list = [column_1, column_2, column_3, column_4, column_5, column_6] 

#This is a tuple, which is an ordered collection of items just like a list, but cannot be changed
buoy_parameters_tuple = (column_1, column_2, column_3, column_4, column_5, column_6)

#You can remove items from a list using the remove() method
buoy_parameters_list.remove(column_1)
print("The parameters we are measuring are: ", buoy_parameters_list) #You can print using the print() function

#You can add items to a list using the append() or insert() method 
buoy_parameters_list.append(column_1) #This will add the item to the end of the list

#This will add the item to the beginning of the list. Lists are indexed starting with 0. 
#By specifying 0 in the line below, column_1 will be added in the first position of the list. 
buoy_parameters_list.insert(0, column_1) 
#You can also add multiple items to a list using the extend() method

#This is a dictionary, which is an unordered collection of items that uses key-value pairs
buoy_parameters_dict = {
    'TIMESTAMP': column_1,
    'External_Temp': column_2,
    'Conductivity_us': column_3,
    'Salinity': column_4,
    'Chlorophyll_RFU': column_5,
    'BGA_PE_RFU': column_6
}

'''
The keys are the names of the parameters in the raw data, 
and the values are the varibles we defined earlier with our naming convention.	
You can access the values in a dictionary using the keys
'''

print(f"The parameters we are measuring are: {buoy_parameters_dict}")
#To print only the values, add .values() to the end of the dictionary
#To print only the keys, add .keys() to the end of the dictionary

'''
Lists, tuples, and dictionaries are all examples of data structures in Python.
They can hold strings (like we have used above) and other data types like integers, floats, and booleans.
An integer is a whole number, a float is a number with a decimal point, and a boolean is either True or False.
'''

# We will try to do a quality control check on some example data. 

# Defining the sensor limits
SENSOR_MAX = 100 #units: RFU, this is an integer
SENSOR_MIN = 0.0 #RFU, this is a float because it has a decimal point
USER_MAX = 50 #RFU, integer
USER_MIN = 5.0 #RFU, float

chlorophyll_ex_data = [10.3, 68.1, 4.4, 71.9, 45.2, 12.5, 0.0, 100.0, 50.0, 5.0] #This is a list of example chlorophyll data in RFU

'''
We are going to use a for loop to iterate through the chlorophyll data and check if the values are within the sensor and user limits.
We will use if-else statements to check the values and print a message if they are outside the sensor and user limits. 
'''

for value in chlorophyll_ex_data: #This is a for loop that will iterate through each value in the chlorophyll_ex_data list
    if value > SENSOR_MAX or value < SENSOR_MIN:
        print(f"Fail sensor limits: {value} RFU") #This will print if the value is outside the sensor limits
    elif value > USER_MAX or value < USER_MIN:
        print(f"This value is outside the user limits: {value} RFU. Check sensor") #This will print if the value is outside the user limits
    else:
        pass

'''
Lets say if one value is outside the sensor limits, the data is not valid and we want to stop the loop.
'''

for value in chlorophyll_ex_data: #This is a for loop that will iterate through each value in the chlorophyll_ex_data list
    if value > SENSOR_MAX or value < SENSOR_MIN:
        break # This will stop the loop if the value is outside the sensor limits
    elif value > USER_MAX or value < USER_MIN:
        print(f"This value is outside the user limits: {value} RFU. Check sensor") #This will print if the value is outside the user limits
    else:
        pass

### PUT BOOLEANS HERE ###
# Booleans are a data type that can only be True or False.
# They are often used in if-else statements to control the flow of the program. 
# For example, we can use a boolean to check if the data is valid or not.

# You can also write functions that perform defined tasks
# The inputs to the function are called an arguments, and the variables within the function are called parameters.

#python has some useful built in functions that can be found in the python library
phycoerythrin_ex_data = [0, 0, 0, 0, 0, 0] #Imagine we got all the same values
print(len(phycoerythrin_ex_data)) #len() and print() are built in python functions. len() tells you the length of the list

'''
Booleans are a data type that can only be True or False.
They are often used in if-else statements to control the flow of the program. 
'''

'''
to write your own function, you first need to define it
the raw data provides dates and time like this: 4/24/25 17:00
but we want the time to be formatted like this 2025-04-24T17:00:00Z which is called ISO 8601 formatting
'''

from datetime import datetime, timezone #datetime is a python module that allows us to use functions and constants from the module

def time_format():
    response = datetime.now() #this will print the current time
    return print(response) #the function needs to be told what the output is
time_format() #for a function to run, it must be called
#if you look at the output, the date is still not in ISO format

def time_format():
    response = datetime.now().isoformat() #this will print the current time in iso format (this is a built in python function)
    return print(response) 
time_format() 

#This is a similar function for some example data

timestamp = ['4/24/25 17:00',
'4/24/25 18:00',
'4/24/25 19:00',
'4/24/25 20:00',
'4/24/25 21:00',
'4/24/25 22:00',
'4/24/25 23:00',
'4/25/25 0:00',
'4/25/25 1:00']

def time_format(list):  
    timestamp_dt = datetime.strptime(timestamp[index], "%m/%d/%y %H:%M") #this will change the values in the timestamp list to datetime format
    timestamp_iso = datetime.isoformat(timestamp_dt) #this will change the values to iso format
    return print(timestamp_iso) 

for index, item in enumerate(timestamp): #we want to go through each item in the list timestamp
    time_format(timestamp)


### Gotta be a better way to do this! ###

# def flat_line_test(phycoerythrin_ex_data):
#     for x in phycoerythrin_ex_data:
#         if not isinstance(x, int) is True:
#             break
#         phycoerythrin_ex_data = iter(phycoerythrin_ex_data)
#         if x != next(phycoerythrin_ex_data):
#             response = "Flat line test passed"
#         elif x != next(phycoerythrin_ex_data):
#             response = "Flat line test passed"
#         else:
#             response = "Flat line detected"
#             break
#     return print(response)

# flat_line_test(phycoerythrin_ex_data)




       
# Booleans : bool()
# True or False



