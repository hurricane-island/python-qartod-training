from ioos_qc import qartod

# QARTOD FLAGS:
# 1 = pass
# 2 = test not run on this data 
# 3 = suspect
# 4 = fail 
# 9 = missing data
import pandas as pd
import random
import numpy
#rate_of_change_check

filepath = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'

WynkenBuouy = pd.read_csv(filepath, header=0, usecols=['Chlorophyll_RFU', 'TIMESTAMP_ISO'])

results_gr = qartod.gross_range_test(
    inp = WynkenBuouy['Chlorophyll_RFU'],
    fail_span = [0, 100],
    suspect_span = [15, 45]
)

import pandas as pd
from pandas import DataFrame, read_csv
from datetime import datetime

file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_2025-05-14T22-45.csv'
site_info = pd.read_csv(file_path, header=0) #reads all of the columns in file
print(site_info.head())

#for our purposes, I only want to read select columns where the column headers are in the second row
df = pd.read_csv(file_path, header=1, usecols =  ["TIMESTAMP", "External_Temp", "Conductivity_us", "SpConductivity_us", "Salinity", "Chlorophyll_ugL", "Chlorophyll_RFU", "BGA_PE_RFU", "BGA_PE_ugL"])

df.drop(0, axis = 0, inplace=True) #I want to drop the first row below the headers which contain units
df.drop(1, axis = 0, inplace=True) #and the second row for analysis purposes 
df = df.reset_index(drop=True) #this resets the index 

timestamp = df["TIMESTAMP"].tolist()

def time_format(list)->list: 
    '''
    This is a function to convert the current time format to ISO 8601 formatting
    '''
    timestamp_dt = [datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S") for timestamp_str in timestamp]
    timestamp_iso = [datetime.isoformat(timestamp_str) for timestamp_str in timestamp_dt]
    return timestamp_iso

timestamp_clean = time_format(timestamp)
df = df.drop("TIMESTAMP", axis='columns') #this drops the old time column in the wrong format
df.insert(loc=0, column = "TIMESTAMP_ISO", value = timestamp_clean) #this inserts the new time column to the leftmost 
print(df.head()) #This prints the first five rows of the dataframe

blank_count = df.isna().sum() #this will count the number of blanks in the df
print(f"Blank count: {blank_count}") 

duplicate_count = df.duplicated().sum() #this will count the number of duplicates in the df
print(f"Duplicate count: {duplicate_count}")

# Save the cleaned DataFrame to a new CSV file
output_file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'
df.to_csv(output_file_path, index=False)

# how you could sort by species
# sorted_by_species = df.sort_values(['header'])

# slice
# copy
# merge




