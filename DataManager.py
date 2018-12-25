# ©PanoPilot®
#
# General Class DataManager
# 
#
# Two Modes: 
#   1. (Loader) loads history data and save it to database
#   2. (Watcher) Watch Live Market and save data to database and throw events according to req. candle timeframe


# Define Custom imports
from Exchanges.Exchange import Exchange
from Exchanges.Kraken_Ex import Kraken_Ex

import json
import pandas as pd
from yahoo_fin.stock_info import *

I_TYPE_Y = "YF"
I_TYPE_W = "WEB"
I_TYPE_E = "EXHANGE"

class DataManager():

    def __init__(self, i_config_f, a_config_f):

        #first read config files
        with open(i_config_f, 'r') as f:
            self.i_config = json.load(f)

        with open(a_config_f, 'r') as f:
            self.a_config = json.load(f) 
 
        #print (self.i_config["IMPORT"]["FROM"])
        #print (exchange, asset, currency)
        #self.exchange_name = exchange
        #self.asset = asset
        #self.currency = currency
        #init exchange
        #REMARK: Switch req. later based on different exchanges 
        #self.exchange = Kraken_Ex()



    #######################################################################
    # 
    # Method to start importing data based on different types
    # Types:
    #   1) WEB:         read data from web/url source
    #   2) yahoo_fin:   usage of yahoo_fin package
    #   3) exchange:    Read data from a exchange API
    #
    # Returns:
    #   
    # 
    ######################################################################## 
    def start_import(self):

        #get assets to import
        symbols = self.a_config["ASSETS"]["SYMBOLS"]
        i_from = self.i_config["IMPORT"]["FROM"]
        i_to = self.i_config["IMPORT"]["TO"]

        #check import source
        if (self.i_config["IMPORT"]["TYPE"] == I_TYPE_Y):
            #ok in this case, use yahoo_fin package
            df_ohlcv = self.yf_import_data_ohlcv(symbols, i_from, i_to)
            #self.save_data_to_hdf(df, "test.h5")

            
        elif(self.i_config["IMPORT"]["TYPE"] == I_TYPE_W):
            pass
        elif(self.i_config["IMPORT"]["TYPE"] == I_TYPE_E):
            pass
    
        #print (df)



    #######################################################################
    # 
    # Method to store a pandas dataframe to a hdf5 file
    # Parameters:
    #   df:         pandas dataframe 
    #   hdf5_file:  full qualified name of hdf5 file
    #
    # 
    ######################################################################## 
    def save_data_to_hdf(self, df, hdf5_file):
        
        hdf = pd.HDFStore(hdf5_file)
        hdf.put('KEY1', df, format='table', data_columns=True)
        hdf.close()


    #######################################################################
    # 
    # Method to import data by using yahoo_fin package
    # Parameters:
    #   symbols: symbols of securities to be imported
    #
    # Returns:   
    #   Pandas Dataframe with imported data
    # 
    ######################################################################## 
    def yf_import_data_ohlcv(self, symbols, ifrom, ito):

        symbols = symbols[:2]
        data = pd.DataFrame([])

        for sym in symbols:
            print('Get Data for:', sym["SYMBOL"])
            data = data.append(get_data(sym["SYMBOL"], start_date = ifrom , end_date = ito, index_as_date=False), )

        #print(data.dtypes)
        #convert to datetime type object
        data['date'] = data['date'].astype('datetime64[ns]')
        #sort values by datetime
        data.sort_values(by=['date'], ascending=True, inplace=True)
        #renew index to date & symbol
        data.reset_index(drop=True, inplace=True)
        data.set_index(['date','ticker'], inplace=True)

        #print(data)
        return data




    def import_ohlcv(self, from_date, to_date):
        #print ('Importing:', self.exchange_name, self.currency, self.asset, 'From:', from_date, 'to', to_date)

        #self.exchange.getHistory_OHLCV(self.asset,self.currency,from_date)

        ##self.exchange.import_ohlcv(self.asset,self.currency,from_date,to_date)
        #self.exchange.getHistory_Trades(self.asset,self.currency,from_date,to_date)
        pass


