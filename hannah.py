# Intro to Python with buoy variables
# Define some variables

column_1 = 'Salinity'
column_2 = 'ODO'
column_3 = 'Turbidity'

buoy_parameters_list = [column_1, column_2, column_3]
print(buoy_parameters_list)

# Remove items from a list
buoy_parameters_list.remove(column_2)
# print(buoy_parameters_list) - shows how to remove, don't want to run 

#Put item back in list
buoy_parameters_list.insert(1,column_2)
# print(buoy_parameters_list) - shows how to put back, don't want to run


# # Dictionaries, items key-value pairs
# buoy_parameters_diction = {
#     "Salinity": column_1,
#     "ODO": column_2,
#     "Turbidity": column_3
# }
# print(f"{buoy_parameters_diction}")


# Quality Assurance Tests - Reasonable value, does data behave as expected?

conductivity_ex_data = [28.9, 24.5, 65.3, 80.4, 76.8, 30.4, 32.6]

SENSOR_MIN = 0         #integer
SENSOR_MAX = 100.00    #float
USER_MIN = 15
USER_MAX = 42

for value in conductivity_ex_data:
    if value > SENSOR_MAX or value < SENSOR_MIN:
        print(f"Fail sensor limits: {value}")
    elif value > USER_MAX or value < USER_MIN:
        print(f"Fail user limits: {value}")
    else:
        pass


# len() - length of list & tuple, print () - prints in output, type() - tells type of data

from datetime import datetime

def time_format ():
    response = datetime.now()   #will print current time
    return print(response)  #print response to SHOW the code was ran
time_format()

def time_format():
    response = datetime.now().isoformat()   #changes to isoformat, helpful b/c hydrosphere data in isoformat
    return print(response)
time_format()
