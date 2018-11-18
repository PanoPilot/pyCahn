
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import subprocess
#import timeit
#import os
#import sys

import datetime

# Define Custom imports
from DataManager import DataManager


if __name__ == "__main__":
    
    data_manager = DataManager("Kraken", "XBT", "EUR")
    
    #print(data_manager.asset, data_manager.exchange_name, data_manager.currency)

    from_time = datetime.datetime(2018, 1, 1)
    to_time = datetime.datetime.now()

    data_manager.import_ohlcv(from_time, to_time)

    #print (from_time, '-->', to_time)