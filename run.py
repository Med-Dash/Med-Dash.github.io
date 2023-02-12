#!/usr/bin/env python

import os
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, 'src')

# Reading in data
from etl import readData
from etl import readOuraData

# Cleaning data
from cleaning import removeNull
from cleaning import cleanColNames
from cleaning import typeCorrectionsOura
from cleaning import typeCorrectionsArboleaf
from cleaning import typeCorrectionsBiomet
from cleaning import colUnitsOura

# Adding features
from features import addWeekend

# Formatting data for Tableau plots
from plot_prep import linePrep
from plot_prep import corrPrep


def main(targets):
    
    config = json.load(open('config/data-params.json'))
    
    # Test target
    if 'test' in targets:
        
        # Cleaning
        testfp  = os.path.join(os.path.join(config['testdata_fp'], 'test_patient'))
        read    = readOuraData(testfp, config['sets'])
        remNull = removeNull(read, 10)
        clean   = cleanColNames(remNull)
        clean   = typeCorrectionsOura(clean)
        clean   = colUnitsOura(clean)
#     clean = typeCorrectionsArboleaf(remNull)
#     clean = typeCorrectionsBiomet(remNull)
        
        # Adding features
        temp = addWeekend(clean)
        
        temp_fp = config['testdata_fp'].replace('raw', 'temp') + '/testdata.csv'
        temp.to_csv(temp_fp)    
            
        # Plot preparation
        out_fp   = temp_fp.replace('temp', 'out').replace('testdata.csv', '') 
        plot_cfg = json.load(open('config/plot-params.json'))
                              
        linePrep(temp_fp, 
                 cols = plot_cfg['line_cols'],
                 output_dir = out_fp,
                 start_date = plot_cfg['start_date'],
                 end_date = plot_cfg['end_date'])
        
        corrPrep(temp_fp, 
                 cols = plot_cfg['corr_cols'],
                 cnames = plot_cfg['corr_col_names'],
                 output_dir = out_fp,
                 start_date = None,
                 end_date = plot_cfg['end_date'])
                 
        
    # Cleaning target
    if 'clean' in targets:
        
        datfp   = os.path.join(os.path.join(config['data_fp'], 'patient'))
        read    = readOuraData(datfp, config['sets'])
        remNull = removeNull(read, 10)
        clean   = cleanColNames(remNull)
        clean   = typeCorrectionsOura(clean)
        clean   = colUnitsOura(clean)
        
        # Adding features
        temp = addWeekend(clean)
        
        temp_fp = config['data_fp'].replace('raw', 'temp') + '/patient.csv'
        temp.to_csv(temp_fp) 
        
    
    # Plot prepping target
    if 'prep' in targets:
        
        temp_fp  = config['data_fp'].replace('raw', 'temp') + '/patient.csv'
        
        out_fp   = temp_fp.replace('temp', 'out').replace('patient.csv', '') 
        plot_cfg = json.load(open('config/plot-params.json'))
                              
        linePrep(temp_fp, 
                 cols = plot_cfg['line_cols'],
                 output_dir = out_fp,
                 start_date = plot_cfg['start_date'],
                 end_date = plot_cfg['end_date']) 
        
        corrPrep(temp_fp, 
                 cols = plot_cfg['corr_cols'],
                 cnames = plot_cfg['corr_col_names'],
                 output_dir = out_fp,
                 start_date = None,
                 end_date = plot_cfg['end_date'])
                                    
    return                           

        
        
if __name__ == '__main__':
    # for testing run via:
    # python run.py test
    #
    # for all data run via:
    # python run.py clean prep
    targets = sys.argv[1:]
    main(targets)
    
    print("Data prepped for plots successfully.")
