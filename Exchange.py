# ©PanoPilot®
#
# General Class Exchange
# 
# Acts as wrapper for several exchange API's
# 

# For now start with Kraken and create a superclass later on based on this

import krakenex

class Exchange():

    def __init__(self):
        #print('Init Exchange')
        pass


    def getHistory_OHLCV(self, asset, currency, from_date, to_date):
        pass

