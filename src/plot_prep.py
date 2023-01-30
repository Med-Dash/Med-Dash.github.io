
import os
import numpy as np
import pandas as pd

from etl import readData



def linePrep(fp, cols, output_dir, start_date=None, end_date='Present'):
    
    '''
    Preps the desired columns for line plotting. Will use a range
    of dates to filter the data.
    
    :param fp: A file path pointing to the cleaned data
    :param cols: A list of columns to prepare for line plotting
    :start_date: A string in the format YYYY-MM-DD. If left as the default
    (None), it will be set to the earliest date available.
    :end_date: A string in the format YYYY-MM-DD. If left as the default
    ('Present'), it will be set to the latest date available.
    :returns: None
    '''
    
    df = readData(fp)
    df = df.assign(date=pd.to_datetime(df['date']))
    date_col = df.columns[df.dtypes.astype(str).str.contains('datetime')][0]
    
    # Setting the start and end Timestamps
    sdate = pd.Timestamp(start_date)
    if pd.isnull(sdate):
        sdate = min(df[date_col])
        
    try:
        edate = pd.Timestamp(end_date)
    except:
        edate = max(df[date_col])
    
    # Prepping the data
    DFS = []
    for x in cols:
        
        fname = x.lower().replace(' ', '') + '_line.csv'
        
        sub = df[[date_col, x]]
        sub = sub.loc[(sub['date'] >= sdate) & (sub['date'] <= edate)]
        
        sub.to_csv(os.path.join(output_dir, fname))
        
        
        
        
        
def corrPrep(fp, cols, output_dir, start_date=None, end_date='Present'):
    
    '''
    Preps the desired columns for correlation line plotting. Will use a 
    range of dates to filter the data.
    
    :param fp: A file path pointing to the cleaned data
    :param cols: A list of two element lists; the inner lists contain pairs 
    of columns that are correlated
    :start_date: A string in the format YYYY-MM-DD. If left as the default
    (None), it will be set to the earliest date available.
    :end_date: A string in the format YYYY-MM-DD. If left as the default
    ('Present'), it will be set to the latest date available.
    :returns: None
    '''
    
    df = readData(fp)
    df = df.assign(date=pd.to_datetime(df['date']))
    date_col = df.columns[df.dtypes.astype(str).str.contains('datetime')][0]
    
    # Setting the start and end Timestamps
    sdate = pd.Timestamp(start_date)
    if pd.isnull(sdate):
        sdate = min(df[date_col])
        
    try:
        edate = pd.Timestamp(end_date)
    except:
        edate = max(df[date_col])
        
    # Prepping the data
    for x in cols:
        
        fname = x[0].lower().replace(' ', '') + '_' + \
                x[1].lower().replace(' ', '') + '_corr.csv'
        
        sub = df[[date_col, x[0], x[1]]]
        sub = sub.loc[(sub['date'] >= sdate) & (sub['date'] <= edate)]
        
        # Calculate the Pearson correlation coefficient
        corr = np.corrcoef(sub[x[0]], sub[x[1]])[0, 1]
        
        sub.to_csv(os.path.join(output_dir, fname))
        
        

