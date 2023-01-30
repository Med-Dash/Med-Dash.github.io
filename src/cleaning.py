
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


