#the purpose of this file is to contain the new code
#The goal of this file is to have code which is more clear and readable.
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


    #symbol = btc_output['Symbol']
    #lp = ticker_input['lastprice']
    #TODO Enter start date as input- ex yyyy-mm-dd
    #TODO Enter End date as input - ex yyyy-mm-dd
    #TODO Enter Interval as input - ex 1d/1 Day
    #TODO Enter Ticker as input - ex TSLA
    #TODO Be able to validate ticker input - is TSLA a valid symbol?
    #TODO Generate barchart based on inputs above

    #ticker_name = "" empty as it will need input.
    #Ticker = yf.Ticker(ticker_name) 
    #print("work on TODO's above.")

def getTickerInfo():
    ticker_input = "BTC-AUD"
    btc_info = yf.Ticker(ticker_input)
    print(f"info: {btc_info.info}")
    



    

def main():
    getTickerInfo()
    



if __name__ == "__main__":
    main()
