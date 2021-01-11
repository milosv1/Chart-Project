import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#################################################
#XRO CHART | ARB CHART | BTC CHART
#TSLA CHART | N/A....  | N/A
#################################################


#The command line holds info such as Close and date (UTC Format) for prices of each stock.


#Firstly, we need to figure out how to get the 2 x 3 charts working, where we 
#have (2) rows x (3) columns containing line charts.

#UTC = YYYY-DAY-MONTH / Just a note.

##-----------------------------------------------
#BTC-AUD 
#ARB.AX
#TSLA
#XRO
#-------------------------------------------------

#My Symbols
btc_aud = yf.Ticker("BTC-AUD")
arb_ax = yf.Ticker("ARB.AX")
xro_ax = yf.Ticker("XRO.AX")
#----------------------------

#History
#first symbol history
data = btc_aud.history(
    start = '2020-01-01',
    end = '2021-10-01',
    interval = "1d")
    
#second symbol history
data1 = arb_ax.history(
    start = '2020-01-01',
    end = '2021-10-01',
    interval = "1d")    

data2 = xro_ax.history(
    start = '2020-01-01',
    end = '2021-10-01',
    interval = "1d"   
)    
#----------------------------

data.sort_values('Date', inplace=True, ascending=True)
data = data[data['Volume']>0] #filter garbage values
data.drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)


data1.sort_values('Date', inplace=True, ascending=True)
data1 = data1[data1['Volume']>0] #filter garbage values
data1.drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)


data2.sort_values('Date', inplace=True, ascending=True)
data2 = data2[data2['Volume']>0] #filter garbage values
data2.drop(['Dividends', 'Stock Splits'], axis=1, inplace=True)


data.head()
data1.head()
data2.head()

#visualization of data, Plotting the price Close. from facecolor w -> b
plt.figure(num=None, 
        figsize=(15, 6), 
        dpi=80, 
        facecolor='w', 
        edgecolor='k')


data['Close'].plot()
data1['Close'].plot()
data2['Close'].plot()


plt.tight_layout()
plt.grid()
plt.show()      


print_ticker = btc_aud
print_ticker1 = arb_ax
print_ticker2 = xro_ax

print_close = data['Close']
print_arb_close = data1['Close']
print_xro_close = data2['Close']


print('Symbol:', print_ticker,
                 print_ticker1,
                 print_ticker2)

print('Close:', '[BTC-AUD]', print_close,
                '[ARB.AX]',print_arb_close,
                '[XRO.AX]',print_xro_close)
