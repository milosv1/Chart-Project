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
    ticker_input_BTC = "BTC-AUD"
    ticker_input_BHP = "BHP.AX"
    btc_info = yf.Ticker(ticker_input_BTC)
    bhp_info = yf.Ticker(ticker_input_BHP)
    owned = 0
    print("Found:")
    for ticker in ticker_input_BHP, ticker_input_BTC:
        owned += 1
        print(f"{owned}:{ticker}")

    #print(f"info: {btc_info.info}\n")
    #print(f"info: {bhp_info.info}\n")



def getTickerPrice():
    print("This function needs work.")

    

def main():
    getTickerInfo()
    getTickerPrice()



if __name__ == "__main__":
    main()
