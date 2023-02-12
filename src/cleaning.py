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



def cleanColNames(df):
    '''
    Converts all columns of a given DataFrame into an easier format to work
    with (all lower case, words separated by underscores)
    
    :param df: DataFrame containing raw Oura Data
    :returns: The DataFrame with cleaned column names
    '''
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df
    
    
  
def typeCorrectionsOura(df):
    '''
    Correct the data types for the raw Oura data
    '''

    #dtype corrections
    #convert time from str to datetime
    df = df.assign(summary_date=pd.to_datetime(df["summary_date"]))
#     df["date"] = pd.to_datetime(df["date"])
#     df["Bedtime Start"] = pd.to_datetime(df["Bedtime Start"])
#     df["Bedtime End"] = pd.to_datetime(df["Bedtime End"])

    #str to float
#     str_to_float = ['Previous Night Score', 'Sleep Balance Score', 'Previous Day Activity Score', 'Activity Balance Score', 'HRV Balance Score', 'Temperature Trend Deviation']
    str_to_float = ['readiness_score_previous_night', 'readiness_score_sleep_balance', 
                    'readiness_score_activity_balance', 'readiness_score_hrv_balance',
                    'sleep_temperature_trend_deviation']
    
    for col in str_to_float:
        df[col] = (df[col]).astype(float)

    #int to float (just for standardization)
    for col in df:
        if df[col].dtype == 'int64':
            df[col] = df[col].astype(float)

    OUT = df.reset_index(drop=True)
    return OUT



def colUnitsOura(df):
    '''
    Edits the column units for raw Oura Data. Currently, sleep duration is 
    being converted from seconds to hours
    
    :param df: DataFrame containing raw Oura data
    :returns: The DataFrame with corrected column units
    '''
    OUT = df.assign(sleep_total_hours = df['sleep_total'].apply(lambda x: (x//3600) \
                                                                + (((x % 3600) // 60)/60)))
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
    Correct the data types for the raw Biometric data (emphasis on Apple Health
    '''
    df["Day"] = pd.to_datetime(df["Day"])
    df["Time"] = pd.to_datetime(df["Time"])

    #removing oura measurements, since we have that in the oura csv
    df = df[~df["Metric"].str.contains("Oura")]

    #nan values - once again, what's the best way to deal with this?
    df = df.dropna()

    OUT = df.reset_index(drop=True)
    return OUT




   
