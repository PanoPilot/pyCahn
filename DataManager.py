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

        #check import source
        if (self.i_config["IMPORT"]["TYPE"] == I_TYPE_Y):
            #ok in this case, use yahoo_fin package
            df = self.yf_import_data_ohlcv(symbols)
        elif(self.i_config["IMPORT"]["TYPE"] == I_TYPE_W):
            pass
        elif(self.i_config["IMPORT"]["TYPE"] == I_TYPE_E):
            pass
    
        #print (df)




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
    def yf_import_data_ohlcv(self, symbols):

        #symbols = symbols[:3]
        data = pd.DataFrame([])

        for sym in symbols:
            print('Get Data for:', sym["SYMBOL"])
            data = data.append(get_data(sym["SYMBOL"],index_as_date=False))
       

        print(data)
        return data




    def import_ohlcv(self, from_date, to_date):
        #print ('Importing:', self.exchange_name, self.currency, self.asset, 'From:', from_date, 'to', to_date)

        #self.exchange.getHistory_OHLCV(self.asset,self.currency,from_date)

        ##self.exchange.import_ohlcv(self.asset,self.currency,from_date,to_date)
        #self.exchange.getHistory_Trades(self.asset,self.currency,from_date,to_date)
        pass


