"""
Example of processing a CSV file with pandas.
"""
from datetime import datetime
from pandas import DataFrame, read_csv

def time_format(ts: list[str]) -> list:
    """
    Convert the current time to ISO 8601 formatting
    """
    timestamp_dt = [
        datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        for timestamp_str in ts
    ]
    timestamp_iso = [
        datetime.isoformat(timestamp_str) for timestamp_str in timestamp_dt
    ]
    return timestamp_iso

file_path = "/Users/adelejordan/Downloads/Wynken_SondeValues_2025-05-14T22-45.csv"
site_info = read_csv(file_path, header=0)  # reads all of the columns in file
print(site_info.head())

# for our purposes, I only want to read select columns where the
# column headers are in the second row
df: DataFrame = read_csv(
    file_path,
    header=1,
    usecols=[
        "TIMESTAMP",
        "External_Temp",
        "Conductivity_us",
        "SpConductivity_us",
        "Salinity",
        "Chlorophyll_ugL",
        "Chlorophyll_RFU",
        "BGA_PE_RFU",
        "BGA_PE_ugL",
    ],
)

df.drop(
    0, axis=0, inplace=True
)  # I want to drop the first row below the headers which contain units
df.drop(1, axis=0, inplace=True)  # and the second row for analysis purposes
df = df.reset_index(drop=True)  # this resets the index

timestamp = df["TIMESTAMP"].tolist()
timestamp_clean = time_format(timestamp)
df = df.drop(
    "TIMESTAMP", axis="columns"
)  # this drops the old time column in the wrong format
df.insert(
    loc=0, column="TIMESTAMP_ISO", value=timestamp_clean
)  # this inserts the new time column to the leftmost
print(df.head())  # This prints the first five rows of the dataframe

blank_count = df.isna().sum()  # this will count the number of blanks in the df
print(f"Blank count: {blank_count}")

duplicate_count = (
    df.duplicated().sum()
)  # this will count the number of duplicates in the df
print(f"Duplicate count: {duplicate_count}")

# Save the cleaned DataFrame to a new CSV file
output_file_path = (
    "/Users/adelejordan/Downloads/Wynken_SondeValues_Cleaned_2025-05-14T22-45.csv"
)
df.to_csv(output_file_path, index=False)

# how you could sort by species
# sorted_by_species = df.sort_values(['header'])

# slice
# copy
# merge
