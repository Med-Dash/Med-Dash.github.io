
import numpy as np
import pandas as pd


def addWeekend(df):
    
    '''
    Adds columns to cleaned Oura data discerning whether or not the day is a weekend
    
    :param df: Cleaned Oura DataFrame
    :returns: Oura DataFrame with 'day_name' and 'is_weekend' columns added
    '''
    

#     OUT = df.assign(date = pd.to_datetime(df['date']))

    OUT = df.assign(date = pd.to_datetime(df['date']))
    OUT = OUT.assign(day_name = OUT['date'].dt.day_name())
    OUT = OUT.assign(is_weekend = OUT['day_name'].isin(['Saturday', 'Sunday']))
    
    return OUT

