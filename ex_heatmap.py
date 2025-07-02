'''
work in progress
'''

import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.dates as mdates

file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'
cleaned_df = pd.read_csv(file_path, header=0)
#print(cleaned_df.head())

#print(cleaned_df.describe()) #The describe function provides summary statistics on each column in the dataframe 

time = cleaned_df["TIMESTAMP_ISO"].to_list()

timestamp_dt = [datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S") for timestamp_str in time]
day = [timestamp_str.day for timestamp_str in timestamp_dt]
#print(day[1])
hour = [timestamp_str.hour for timestamp_str in timestamp_dt]
#print(hour[1])

data = pd.DataFrame({
    'day': day,
    'hour': hour,
    'Chlorophyll': cleaned_df["Chlorophyll_RFU"].to_list()
})

print(data.head())


plt.figure(figsize=(4,3))
plt.imshow(data, cmap='viridis', vmin = 0, vmax = 1)
plt.colorbar()
plt.show()




# time_dt = pd.to_datetime(time)
# months = mdates.MonthLocator()
# hours = mdates.HourLocator()

# print(type(time_dt))
# chlorophyll = cleaned_df["Chlorophyll_RFU"].to_list()

# time_dt = datetime(time_dt)
# print(type(time_dt))
# month = time_dt.month
# print(month)