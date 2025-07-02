'''
WORK IN PROGRESS
NEEDS COMMENTS
'''


import pandas as pd
from pandas import DataFrame, read_csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.dates as mdates

file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'
cleaned_df = pd.read_csv(file_path, header=0)
#print(cleaned_df.head())

#print(cleaned_df.describe()) #The describe function provides summary statistics on each column in the dataframe 

time = cleaned_df["TIMESTAMP_ISO"].to_list()
time_dt = pd.to_datetime(time)
chlorophyll = cleaned_df["Chlorophyll_RFU"].to_list()


fig, ax = plt.subplots(figsize=(4, 3))

plt.xlabel('Timestamp')
plt.ylabel('Chlorophyll (RFU)')
plt.title("Time series analysis example")
plt.xticks(rotation=45)
plt.ylim(0,1.5)
plt.xlim(datetime(2025,5,1,9,0), datetime(2025, 5, 10, 10, 0))
plt.gcf().autofmt_xdate() 
# ax.xaxis.set_major_locator(mdates.DayLocator(0, interval=30)) #for this to work, need to convert back to datetime
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m'))
plt.axvspan(datetime(2025, 5, 1, 12, 0), datetime(2025, 5, 3, 12, 0), color='red', alpha=0.3)


plt.plot(time_dt, chlorophyll, color='r', linewidth=1.0, linestyle='-', label = 'chlorophyll') 


plt.legend(loc='upper right')
plt.show()
plt.savefig('path/name.pdf') #example of saving the plot as a pdf


###check a daily trend?

###Add another series

###Add chlorophyll from Blynken

###Subplots

# fig, ax1 = plt.subplots(figsize=(4, 3))
# ax1_set_xlabel = 
# ax1_set_ylabel = 
# ax2 = fig.add_axes