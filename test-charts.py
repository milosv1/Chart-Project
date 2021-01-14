import yfinance as yf
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plot

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


#################################################
#XRO CHART | ARB CHART | BTC CHART
#TSLA CHART | N/A....  | N/A
#################################################

#Quick note to self:
#The charts can even be arranged like this:
#  | XRO CHART
#  | ARB CHART
#  | BTC CHART
#  | TSLA CHART 

#The command line holds info such as Close and date (UTC Format) for prices of each stock.

#print("this is an added file which works as a testing ground for data \n - and charts.")

#our symbols:
btc_aud = yf.ticker("BTC-AUD")

#Must be in UTF format due to yfinance library.
#Start & End dates of Symbols:
data_btc = btc_aud.history(
    start = '2020-01-01',
    end = '2021-14-01',
    interval = '1d'
)
