import numpy as np
import pandas as pd


def removeNull(df, thresh):
    
    '''
    Removes null values based on a threshold

    :param df: DataFrame containing raw Oura Data
    :param thresh: Number of missing values acceptable for each row (if number of NaN 
    values exceeds thresh, the entire row will be deleted)
    :returns: A cleaned DataFrame
    '''

    over = (df.isna().sum(axis=1) > thresh)
    OUT  = df.loc[~over]

    return OUT
  
  
def typeCorrectionsOura(df):
    '''
    Correct the data types for the raw Oura data
    '''

    #dtype corrections
    #convert time from str to datetime
#     df = df.assign(date=pd.to_datetime(df["date"]))
#     df = df.assign(Bedtime Start=pd.to_datetime(df["Bedtime Start"]))
#     df = df.assign(Bedtime End=pd.to_datetime(df["Bedtime End"]))
    df["date"] = pd.to_datetime(df["date"])
    df["Bedtime Start"] = pd.to_datetime(df["Bedtime Start"])
    df["Bedtime End"] = pd.to_datetime(df["Bedtime End"])

    #str to float
    str_to_float = ['Previous Night Score', 'Sleep Balance Score', 'Previous Day Activity Score', 'Activity Balance Score', 'HRV Balance Score', 'Temperature Trend Deviation']
    for col in str_to_float:
        df[col] = (df[col]).astype(float)

    #int to float (just for standardization)
    for col in df:
        if df[col].dtype == 'int64':
          df[col] = df[col].astype(float)

    OUT = df.reset_index(drop=True)
    return OUT


def typeCorrectionsArboleaf(df):
    '''
    Correct the data types for the raw Arboleaf data
    '''
    #filling nan values
    df = df.drop(columns=["Muscle storage ability level"])

    #str to datetime
    df['Time of Measurement'] = df['Time of Measurement'].str.replace('，', '').str.replace(" at ", " ")
    df['Time of Measurement'] = pd.to_datetime(df['Time of Measurement'])

    OUT = df.reset_index(drop=True)
    return OUT

def typeCorrectionsBiomet(df):
    '''
    Correct the data types for the raw Bimetric data (emphasis on Apple Health
    '''
    df["Day"] = pd.to_datetime(df["Day"])
    df["Time"] = pd.to_datetime(df["Time"])

    #removing oura measurements, since we have that in the oura csv
    df = df[~df["Metric"].str.contains("Oura")]

    #nan values - once again, what's the best way to deal with this?
    df = df.dropna()

    OUT = df.reset_index(drop=True)
    return OUT
   
