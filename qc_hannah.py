
from ioos_qc import qartod
import pandas as pd
from pandas import DataFrame, read_csv
from datetime import datetime

file_path = 'RG.csv'
df: DataFrame = pd.read_csv(file_path, header=0) #reads all of the columns in file
chlorophyll = df['Chlorophyll_RFU']
# print (site_info.head())

# df = df.reset_index(drop=True) #this resets the index 

# timestamp = df["TIMESTAMP"].tolist()

# def time_format(list)->list: 
#     '''
#     This is a function to convert the current time format to ISO 8601 formatting
#     '''
#     timestamp_dt = [datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S") for timestamp_str in timestamp]
#     timestamp_iso = [datetime.isoformat(timestamp_str) for timestamp_str in timestamp_dt]
#     return timestamp_iso

# timestamp_clean = time_format(timestamp)
# df = df.drop("TIMESTAMP", axis='columns') #this drops the old time column in the wrong format
# df.insert(loc=0, column = "TIMESTAMP_ISO", value = timestamp_clean) #this inserts the new time column to the leftmost 
# print(df.head()) #This prints the first five rows of the dataframe

blank_count = df.isna().sum() #this will count the number of blanks in the df
# print(f"Blank count: {blank_count}") 

duplicate_count = df.duplicated().sum() #this will count the number of duplicates in the df
# print(f"Duplicate count: {duplicate_count}")

# Save the cleaned DataFrame to a new CSV file
# output_file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'
# df.to_csv(output_file_path, index=False)

# how you could sort by species
# sorted_by_species = df.sort_values(['header'])

# slice
# copy
# merge

# QARTOD FLAGS:
# 1 = pass
# 2 = test not run on this data 
# 3 = suspect
# 4 = fail 
# 9 = missing data

results_gr = qartod.gross_range_test(
    inp = chlorophyll,
    fail_span = [0, 100],
    suspect_span = [0, 5]
)
suspect_fail_data = (results_gr>2).sum()
print(suspect_fail_data)

# print(df.describe())

# Results Spike
results_spike = qartod.spike_test(
    inp = chlorophyll,
    suspect_threshold = 0.25,
    fail_threshold = 0.5,
    method = "average"
    
)
suspect_fail_spike = (results_spike>2).sum()
print("suspect or fail", suspect_fail_spike)
print("fail", (results_spike==4).sum())


