
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import subprocess
#import timeit
#import os
import sys
import getopt

import datetime
import json

# Define Custom imports
from DataManager import DataManager


MODE_TEST = 1
MODE_IMPORT = 2
MODE_WATCH = 3
MODE_TRADE = 4

#######################################################################
# 
# Method to check and parse Command Line Argurments (cla)
# Parameters:
#   argv : command line arquements
#
# Returns:
#   1) mode = <MODE_TEST | MODE_IMPORT | MODE_WATCH |MODE_TRADE>
#   2) name of mode config file
#   3) name of asset config file
# 
######################################################################## 
def check_cla(argv):
    #  -backtest: -import: -watch: -trade: -asset:
    mode = 0
    mode_config = ""
    asset_config = ""

    try:
        opts, args = getopt.getopt(argv,"hb:i:w:t:a:", ["backtest=", "import=", "watch=", "trade=", "asset="])
    except getopt.GetoptError as err:
        print(err)
        print('pyCahn.py [-backtest=config-file -import=config-file -watch=config-file -trade=config-file] -asset=config-file')
        print('pyCahn.py [-b <config-file> -i <config-file> -w <config-file> -t <config-file>] -asset=config-file')
        print('Only one mode possible [-backtest -import -watch -trade]')
        sys.exit(2)
      
    for opt, arg in opts:
        if opt == '-h':
            print('pyCahn.py [-backtest=config-file -import=config-file -watch=config-file -trade=config-file] -asset=config-file')
            print('pyCahn.py [-b <config-file> -i <config-file> -w <config-file> -t <config-file>] -asset=config-file')
            print('Only one mode possible [-backtest -import -watch -trade]')
            sys.exit()
        elif opt in ("-b", "--backtest"):
            if mode!=0:
                print('ERROR: Only one mode possible [-backtest -import -watch -trade]')
                sys.exit() 
            mode_config = arg
            mode = MODE_TEST
        elif opt in ("-i", "--import"):
            if mode!=0:
                print('ERROR: Only one mode possible [-backtest -import -watch -trade]')
                sys.exit() 
            mode_config = arg
            mode = MODE_IMPORT
        elif opt in ("-w", "--watch"):
            if mode!=0:
                print('ERROR: Only one mode possible [-backtest -import -watch -trade]')
                sys.exit() 
            mode_config = arg
            mode = MODE_WATCH
        elif opt in ("-t", "--trade"):
            if mode!=0:
                print('ERROR: Only one mode possible [-backtest -import -watch -trade]')
                sys.exit() 
            mode_config = arg
            mode = MODE_TRADE
        elif opt in ("-a", "--asset"):
            asset_config = arg

    if (mode_config == "" or asset_config == ""):
        print('ERROR: No mode or asset config file provided')
        sys.exit()

    return mode, mode_config, asset_config


#######################################################################
# 
# Method to handle import of data and stores it to hdf file
# Parameters:
#   i_config: name of mode config file
#   a_config: name of asset config file
#
# Returns:
#   
# 
######################################################################## 
def handle_import(i_config, a_config):
    #init Datamanager
    dm = DataManager(i_config, a_config)
    
    #start import
    dm.start_import()

#######################################################################
# 
# Main method 
#
# Supported Modes:
#   1) Backtesting of strategies
#   2) Importing of data
#   3) Realtime watching and updating of asset data
#   4) Realtime trading of assets with given strategie
#   
######################################################################## 
if __name__ == "__main__":
    
    # we need an argument parser at this place
    mode, mode_config, asset_config = check_cla(sys.argv[1:])

    # Check mode
    if mode == MODE_IMPORT:
        handle_import(mode_config, asset_config)    
    elif mode == MODE_TEST:
        pass
    elif mode == MODE_TRADE:
        pass
    elif mode == MODE_TRADE:
        pass
    #print(mode, mode_config, asset_config)
    #data_manager_krak = DataManager("Kraken", "ETH", "EUR")
    #data_manager_krak.import_ohlcv(from_time, to_time)