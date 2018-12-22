# ©PanoPilot®
#
# General Class Exchange
# 
# Acts as wrapper for several exchange API's
# 

# For now start with Kraken and create a superclass later on based on this

import datetime
import calendar
import time

class Exchange():

    def __init__(self):
        pass

    def getHistory_OHLCV(self, asset, currency, from_date):
        pass

    def getHistory_Trades(self, asset, currency, from_date, to_date):
        pass

    # takes date and returns nix time
    def date_nix(self, str_date):
        return calendar.timegm(str_date.timetuple())

    # takes nix time and returns date
    def date_str(self, nix_time):
        return datetime.datetime.fromtimestamp(nix_time).strftime('%m, %d, %Y')