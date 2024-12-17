import pandas as pd 


def read(path):
    # read csv file
    # df['date'] = pd.to_datetime(df['date'], format = 'coerce') and return the dataframe
    return pd.read_csv(path)