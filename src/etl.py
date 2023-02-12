import os
import numpy as np
import pandas as pd
import requests
import json


################################### Used for reading in csv data ##################################


def readData(fp):
    '''
    Given a file path, reads in a set of data
    '''
    
    OUT = pd.read_csv(fp, index_col=[0])
    
    if OUT.index.name:
        OUT = OUT.reset_index()
        
    return OUT


############### Used for concatenating Oura Data (if split into multiple files) ###################

def readOuraData(fp, sets):
    '''
    Given a file path pointing to a directory with Oura files, concatenates
    a set of data
    
    :param fp: A file path pointing to a directory of Oura data files
    :param sets: A list of strings containing the desired data sets to concatenate.
    The sleep dataset will always be included, so this should not be included in the
    list.
    '''
    files = os.listdir(fp)
    
    fnames = {}
    for x in files:
        name = x.replace('test_', '').replace('.csv', '')
        fnames[name] = x
        
    
    # Read in the sleep data, rename the columns for merging)
    OUT = readData(os.path.join(fp, fnames['sleep']))
    OUT.columns = 'sleep_' + OUT.columns
    OUT = OUT.rename(columns={'sleep_summary_date':'summary_date'})
                   
    # Repeat a similar process for the other specified datasets, and concatentate
    for y in sets:
        df  = readData(os.path.join(fp, fnames[y]))
        df.columns = y + '_' + df.columns
        df = df.rename(columns={y + '_summary_date':'summary_date'})
        OUT = pd.merge(OUT, df, how='left', on='summary_date')
        
    return OUT
    

################################## Used for reading in API data ###################################


def make_request(var, start_date, end_date, PAT):
    '''
    Uses the specfied parameters to extract data from Oura
    
    :param var: The type of data to extract
    :param start_date: The earliest date from the data to be extracted
    :param end_date: The most recent date from the data to be extracted
    :param PAT: The personal access token for one patient
    :returns: A string containing the extracted data in json format
    '''
    
    url = f"https://api.ouraring.com/v2/usercollection/{var}" 
    params={ 
        "start_date": start_date, 
        "end_date": end_date 
    }
    headers = { 
      "Authorization": f"Bearer {PAT}" 
    }
    response = requests.request("GET", url, headers=headers, params=params) 
    return response.text


def format_text(text):
    
    '''
    Takes the text output of make_request and formats it into a DataFrame
    
    :param text: The extracted data as a string
    :returns: A DataFrame containing the requested data
    '''
    
    # Conver the string to json
    obj  = json.loads(text)
    temp = pd.DataFrame(obj["data"])
    
    # Divide the DataFrame into two pieces and append back together
    try:
        DF1 = temp.drop("contributors", axis = 1)
        DF2 = pd.DataFrame(list(temp["contributors"].values))
    
        OUT = pd.concat([DF1, DF2], axis = 1)
    
    # Exception for heart rate data
    except:
        OUT = temp
        
    return OUT


################################### Used for reading in S3 data ####################################

# TODO
