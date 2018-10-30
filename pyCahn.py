
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import subprocess
import timeit
import os
import sys




if __name__ == "__main__":
    # by default store results to this file
    scen_df_store_file = "gekko_store.h5"
    mode = 'gen'
    template_filename = ''
    