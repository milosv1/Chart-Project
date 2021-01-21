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
btc_aud = yf.Ticker("BTC-AUD")

#Must be in UTF format due to yfinance library.
#Start & End dates of Symbols:
data_btc = btc_aud.history(
    start = '2020-01-01',
    end = '2021-01-21',
    interval = '1d'
)

data_btc.sort_values('Date', inplace=True, ascending=True)
data_btc = data_btc[data_btc['Volume']>0] #filter garbage values
data_btc.drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)

data_btc.head()

plot.figure(num=None, 
        figsize=(15, 6), 
        dpi=80, 
        facecolor='w', 
        edgecolor='k')

data_btc['Close'].plot()

plot.title('BTC-AUD', loc='center')
plot.tight_layout()
plot.grid()
plot.show()  

#printcur_btc_aud_price = data_btc['Close']
#print(f'{printcur_btc_aud_price}') 

#print final price
last_price = (data_btc.tail(1)['Close'].iloc[0])
print(btc_aud,last_price)
## -------------------------------