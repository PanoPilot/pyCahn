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
        self.exchange_name = exchange
        self.asset = asset
        self.currency = currency

        #init exchange
        self.kraken = Exchange()


 

    def import_ohlcv(self, from_date, to_date):
        print ('Importing:', self.exchange_name, self.currency, self.asset, 'From:', from_date, 'to', to_date)

        self.kraken.getHistory_OHLCV(self.asset,self.currency,from_date,to_date)
        


