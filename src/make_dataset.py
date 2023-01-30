

import os
import sys
import json
import numpy as np
import pandas as pd

from etl import readData
from cleaning import removeNull
from features import addWeekend
from plot_prep import linePrep


def main(targets):
    
    config = json.load(open('../config/data-params.json'))
    
    if 'test' in targets:
        fp_var = 'testdata_fp'
        
    if 'all' in targets:
        fp_var = 'data_fp'
    
    # Data cleaning, saved to temp folder
    read  = readData(config[fp_var])

    remNull = removeNull(read, 10)
    clean = typeCorrectionsOura(remNull)
#     clean = typeCorrectionsArboleaf(remNull)
#     clean = typeCorrectionsBiomet(remNull)

    temp  = addWeekend(clean)
        
    temp_fp = config[fp_var].replace('raw', 'temp')
    temp.to_csv(temp_fp)
    
    # Plot preparation, saved to out folder
    out_fp   = temp_fp.replace('temp', 'out').replace('testdata.csv', '')
    plot_cfg = json.load(open('../config/plot-params.json'))
        
    linePrep(temp_fp, 
             cols = plot_cfg['cols'],
             output_dir = out_fp,
             start_date = plot_cfg['start_date'],
             end_date = plot_cfg['end_date'])
    
        
        
if __name__ == '__main__':
    # run via:
    # python make_dataset.py test
    targets = sys.argv[1:]
    main(targets)
    
    print("Data prepped for plots successfully.")
