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


filepath = '/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv'

WynkenBuouy = pd.read_csv(filepath, header=0, usecols=['Chlorophyll_RFU', 'TIMESTAMP_ISO']) #This imports the two columns timestamp and chlorophyll into a dataframe

results_gr = qartod.gross_range_test(
    inp = WynkenBuouy['Chlorophyll_RFU'],
    fail_span = [0, 100],
    suspect_span = [15, 45]
)
