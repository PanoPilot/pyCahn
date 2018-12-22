# ©PanoPilot®
#
# Class for Kraken Exchange using the krakenex package from github
# 
# 
# 

import krakenex
import pandas as pd
import numpy as np
import time

from Exchanges.Exchange import Exchange

class Kraken_Ex(Exchange):
 

    def __init__(self):
        super().__init__()
        self.krak_api = krakenex.API()
        

    def getHistory_OHLCV(self, asset, currency, from_date):
        
        pair = 'X'+asset+'Z'+currency
        since = from_date
        interval = 5


        #ret = self.krak_api.query_public('AssetPairs')
        ret = self.krak_api.query_public('OHLC', data = {'pair': pair, 'interval': interval, 'since': since})
        data = np.array(ret['result'][pair])

        #print (data[:,:5])
        #print (data[:,6])
        # cut out vwap and count from result list
        df = pd.DataFrame(np.column_stack([data[:,:5],data[:,6]]), columns=('time', 'open', 'high', 'low', 'close', 'volume'))

        
        df['time'] = pd.to_datetime(df['time'], unit='s')
        print (df)
        

    def getHistory_Trades(self, asset, currency, from_date, to_date):
        
        pair = 'X'+asset+'Z'+currency
        since = Exchange.date_nix(self, from_date)
        count = 1 # init value

        data_th = np.zeros((1,6))

        while count > 0:
            ret = self.krak_api.query_public('Trades', data ={'pair': pair, 'since': since})
            data = np.array(ret['result'][pair])
            since = ret['result']['last']
            count = data.shape[0]

            #df = pd.DataFrame(data[:,:4], columns=('price', 'volume', 'time', 'buy/sell'))
            #df['time'] = pd.to_datetime(df['time'], unit='s')
            data_th = np.vstack([data_th, data])

            time.sleep(1)

        df = pd.DataFrame(data_th[:,:3], columns=('price', 'volume', 'time'))
        df['time'] = pd.to_datetime(df['time'], unit='s')
        print(df)


