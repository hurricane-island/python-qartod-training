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

time = cleaned_df["TIMESTAMP_ISO"].to_list() #This will be our x-axis
time_dt = pd.to_datetime(time)
chlorophyll = cleaned_df["Chlorophyll_RFU"].to_list() # This will be our y-axis

fig, ax = plt.subplots(figsize=(4, 3)) #specifies that we are making a figure of size 4 rows x 3 columns 

plt.xlabel('Timestamp')
plt.ylabel('Chlorophyll (RFU)')
plt.title("Time series analysis example")
plt.xticks(rotation=45)
plt.ylim(0,1.5)
plt.xlim(datetime(2025, 5, 1, 9, 0), datetime(2025, 5, 10, 10, 0)) #I only wanted to look at this time period
plt.gcf().autofmt_xdate() # helpful feature of matplotlib that autofits dates into the x-axis
plt.axvspan(datetime(2025, 5, 1, 12, 0), datetime(2025, 5, 3, 12, 0), color='red', alpha=0.3) # This provides the red shading to emphasize one period within the figure
plt.plot(time_dt, chlorophyll, color='r', linewidth=1.0, linestyle='-', label = 'chlorophyll') #time_dt = x and chlorophyll = y with stylistic features! 
plt.legend(loc='upper right') # The legend will look for "label" in the plot line

plt.show()
plt.savefig('path/name.pdf') #example of saving the plot as a pdf


###check a daily trend?

###Add another series

###Add chlorophyll from Blynken

###Subplots

###heat map?