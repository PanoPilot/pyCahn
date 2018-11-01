# ©PanoPilot®
#
# General Class DataManager
# 
#
# Two Modes: 
#   1. (Loader) loads history data and save it to database
#   2. (Watcher) Watch Live Market and save data to database and throw events according to req. candle timeframe


# Define Custom imports
from Exchange import Exchange

class DataManager():

    def __init__(self, exchange, asset, currency):

        #HERE: add a check of suppored exchanges assets etc!

        #print (exchange, asset, currency)
        self.exchange = exchange
        self.asset = asset
        self.currency = currency

        #init exchange
        self.exchange = Exchange()


 

    def import_ohlcv(self, from_time, to_time):
        pass
