from ioos_qc import qartod, utils, plotting
import pandas as pd
from ioos_qc.qartod import aggregate, ClimatologyConfig, gross_range_test, climatology_test
from ioos_qc.config import Config, ContextConfig
from ioos_qc.streams import PandasStream
from ioos_qc.results import collect_results, CollectedResult, collect_results_list, collect_results_dict
from ioos_qc.stores import PandasStore
import matplotlib.pyplot as plt
from datetime import datetime


#1. Getting data to test
file_path = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv' # REPLACE WITH FILE PATH

data = pd.read_csv(file_path, header = 0) # REPLACE WITH HEADER IF NECESSARY

'''
In stream below, replace with names of the time, depth, latitude, and longitude column 
'''

stream = PandasStream(data, time = 'TIMESTAMP_ISO', z = "Depth", lat = "Lat", lon = "Long", geom = None)   


#2. Defining configuration for location and gross range tests for each variable
# Wynken bbox : [-68.887, 44.038, -68.897, 44.048]
# Blynken bbox : [-68.922, 44.313, -68.932, 44.323]

config = """
        streams:
            External_Temp:
                qartod:
                    location_test:
                        bbox: [-68.887, 44.038, -68.897, 44.048] 
                    gross_range_test:
                        suspect_span: [0.56, 22]
                        fail_span: [-5, 50]
            Conductivity_us:
                qartod:
                    location_test:
                        bbox: [-68.887, 44.038, -68.897, 44.048] 
                    gross_range_test:
                        suspect_span: [15000, 35000]
                        fail_span: [0, 100000]
            ODO_Sat:
                qartod:
                    location_test:
                        bbox: [-68.887, 44.038, -68.897, 44.048] 
                    gross_range_test:
                        suspect_span: [90, 120]
                        fail_span: [0, 500]
            Chlorophyll_RFU:
                qartod:
                    location_test:
                        bbox: [-68.887, 44.038, -68.897, 44.048]
                    gross_range_test:
                        suspect_span: [0, 5]
                        fail_span: [0, 100]
            BGA_PE_RFU:
                qartod:
                    location_test:
                        bbox: [-69, 43, -67, 45]
                    gross_range_test:
                        suspect_span: [0, 5]
                        fail_span: [0, 100]
"""

c = Config(config)

#3 Running the tests on the data
flags = stream.run(c)

#4 Appending the QC flags onto the dataframe
store = PandasStore(flags, axes = None)
new_df = store.save(write_data=True, write_axes=True, include= None, exclude=None)

#5 Plotting the results

def plot_qc_results(df, time_col, var_col, qc_test_col, title):
    '''
    df = Dataframe containing the data
    time_col = Name of column containing time data
    var_col = Name of column containing the variable data 
    qc_test_col = Name of the column containing the QC test results
    title = Title of the plot
    '''
    time = pd.to_datetime(df[time_col].tolist())
    var = df[var_col].tolist()
    for i in range(len(var)):
        if df[qc_test_col][i] == 4:
            plt.scatter(time[i], var[i], marker = 'o', color = 'red')
        elif df[qc_test_col][i] ==3:
            plt.scatter(time[i], var[i], marker = 'o', color = 'orange')
        elif df[qc_test_col][i] == 2:
            plt.scatter(time[i], var[i], marker = 'o', color = 'gray')
        elif df[qc_test_col][i] == 1:
            plt.scatter(time[i], var[i], marker = 'o', color = 'green')
        else:
            plt.scatter(time[i], var[i], marker = 'o', color = 'blue')
    plt.plot(time, var, color='lightgray', linewidth=0.5, linestyle='-', label = var_col)
    plt.xlabel('Time')
    plt.ylabel(var_col)
    plt.title(title)
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

#plot_qc_results(new_df, 'time', 'External_Temp', 'External_Temp_qartod_gross_range_test', 'QC Test for Temp')

'''
#6 Running the climatology test
'''
x = len(data['TIMESTAMP_ISO'])

new_config = qartod.ClimatologyConfig(members = None)
params = {
    'tspan': [pd.to_datetime(data['TIMESTAMP_ISO'][0]), data['TIMESTAMP_ISO'][x-1]], #timespan you would like climatology test to run
    'vspan' : [0.56, 13.3], # outside this range will be flagged as suspect
    'fspan': [0.56, 22], # outside this range will be flagged as fail
    'zspan' : None, # depth span
    'period' : None # the period you choose to run the climatology test over, if included need to change the tspan
    }
    
new_config.add(**params)

results_cc = qartod.climatology_test(
            config = new_config,
            inp = data["External_Temp"],
            tinp = data["TIMESTAMP_ISO"],
            zinp = data['Depth']
)

data['external_temp_climatology_test'] = results_cc #adds the climatology test flags to the dataframe 

#7 Plotting the climatology test results
#plot_qc_results(data, 'TIMESTAMP_ISO', 'External_Temp', 'external_temp_climatology_test', 'Climatology Test for Temp')









