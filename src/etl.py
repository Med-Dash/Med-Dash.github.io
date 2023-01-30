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
