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
        datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S") for timestamp_str in ts
    ]
    timestamp_iso = [
        datetime.isoformat(timestamp_str) for timestamp_str in timestamp_dt
    ]
    return timestamp_iso

def head(filename: str) -> None:
    """
    Example of reading a CSV file and printing the first few rows.
    """
    df: DataFrame = read_csv(filename, header=0)
    print(df.head())

def select_columns(filename: str, columns: list[str]) -> DataFrame:
    """
    Read a CSV file and select specific columns.
    """
    # for our purposes, I only want to read select columns where the
    # column headers are in the second row
    df: DataFrame = read_csv(filename, header=1, usecols=columns)

    # drop the first row below the headers which contain units
    df.drop(0, axis=0, inplace=True)

    # and the second row for analysis purposes
    df.drop(1, axis=0, inplace=True)

    # resets the index
    df = df.reset_index(drop=True)

    timestamp = df["TIMESTAMP"].tolist()
    timestamp_clean = time_format(timestamp)

    # drops the old time column in the wrong format
    df = df.drop("TIMESTAMP", axis="columns")

    # inserts new time column leftmost
    df.insert(loc=0, column="TIMESTAMP_ISO", value=timestamp_clean)

    return df

def show_blank_and_duplicate_counts(df: DataFrame) -> None:
    """
    Print the number of blanks and duplicates in the DataFrame.
    """
    blank_count = df.isna().sum()
    print(f"Blank count: {blank_count}")

    duplicate_count = df.duplicated().sum()  # count the number of duplicates in the df
    print(f"Duplicate count: {duplicate_count}")

if __name__ == "__main__":
    EXAMPLE = "data/Wynken_SondeValues_2025-05-14T22-45.dat"
    OUTPUT = "data/sonde-observations.csv"
    COLUMNS = [
        "TIMESTAMP",
        "External_Temp",
        "Conductivity_us",
        "SpConductivity_us",
        "Salinity",
        "Chlorophyll_ugL",
        "Chlorophyll_RFU",
        "BGA_PE_RFU",
        "BGA_PE_ugL",
    ]
    head(EXAMPLE)
    cleaned = select_columns(EXAMPLE, COLUMNS)
    print(cleaned.head())  # print the first five rows
    show_blank_and_duplicate_counts(cleaned)
    cleaned.to_csv(OUTPUT, index=False)
