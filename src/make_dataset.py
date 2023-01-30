

import os
import numpy as np
import pandas as pd

from etl import readData
from cleaning import removeNull
from features import addWeekend
from plot_prep import linePrep


def main(targets):
    
    config = json.load(open('config/data-params.json'))
    
    if 'test' in targets:
        fp_var = 'testdata_fp'
        
    if 'all' in targets:
        fp_var = 'data_fp'
    
    
    # Data cleaning, saved to temp folder
    read  = readData(config[fp_var], 10)
    clean = removeNull(read)
    temp  = addWeekend(clean)
        
    temp_fp = config[fp_var].replace('raw', 'temp')
    temp.to_csv(temp_fp)
    
    # Plot preparation, saved to out folder
    out_fp   = temp_fp.replace('temp', 'out')
    plot_cfg = json.load(open('config/plot-params.json'))
        
    plot_prep(temp_fp, 
              cols = plot_cfg['cols'],
              start_date = plot_cfg['start_date'],
              end_date = plot_cfg['end_date'])
    
        
        
if __name__ == '__main__':
    # run via:
    # python make_dataset.py test
    targets = sys.argv[0:]
    main(targets)
