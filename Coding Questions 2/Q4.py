import yfinance as yf
import pandas as pd
import numpy as np

def main():
    print("Program that finds the longest period a stock was up in 2020")
    
    stock = input("Please enter the stock symbol: ")
    
    stock_df = yf.download(stock, start = '2020-01-01', end = '2020-12-31', progress = False)
    
    close_df = stock_df['Close']
    #date = stock_df[r'\ndate']
    date_df = list(close_df.index)
    
    count = max_up(close_df,date_df)
    print(f'\nThe longest up period for the stock symbol {stock.upper()}:')
    print('{:30} {}'.format('Length in days:',str(count[0])))
    print('{:30} {}'.format('Period started on:',str(count[1])))
    print('{:30} {}'.format('Close stock value at start:',str(np.round(count[2],2))))
    print('{:30} {}'.format('Period ended on:',str(count[3])))
    print('{:30} {}'.format('Close stock value at end:',str(np.round(count[4],2))))
    
def max_up(stock,date):
    count = [] #[(days,start,end),(),()...]
    days = 0
    sdate = 0
    sclose = 0
    edate = 0
    eclose = 0
    for i in range(1, len(stock)):
        if sdate == 0: 
            sdate = str(date[i].date())
            sclose = stock[i]
            edate = str(date[i].date())
            eclose = stock[i]
            
        if (stock[i] - stock[i-1]) > 0.0:
            days +=1
            edate = str(date[i].date())
            eclose = stock[i]
        else:
            count.append((days,sdate,sclose,edate,eclose))
            sdate = 0
            sclose = 0
            days = 0
            edate = 0
            eclose = 0
    count.sort(key = lambda x: x[0], reverse = True)
    return count[0]


main()
