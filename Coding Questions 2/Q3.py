import yfinance as yf
import pandas as pd 
import numpy as np

def main(): 
    
    print("Program calculates sample coorelation between Boeing and CocaCola closing stock values in 2020")
    print()
    
    ba_df = yf.download('BA', start = '2020-01-01', end = '2020-12-31', progress = False)
    ko_df = yf.download('KO', start = '2020-01-01', end = '2020-12-31', progress = False)
    
    mean_ba = sum(ba_df['Close'])/len(ba_df['Close'])
    
    mean_ko = sum(ko_df['Close'])/len(ko_df['Close'])
    
    mean_ba = np.round(mean_ba, 2) 
    mean_ko = np.round(mean_ko, 2) 
    
    ba_closing = (ba_df['Close'])
        
    ko_closing = (ko_df['Close'])
    
    std1 = std(ba_closing)
    std1 = np.round(std1, 2)
    
    std2 = std(ko_closing)
    std2 = np.round(std2,2)
    
    
    print("Average Boeing stock value: \t", mean_ba)
    print("Std of Boeing stock: \t", std1)
    print()
    
    print("Average Coke stock value: \t", mean_ko)
    print("Std of Coke stock: \t", std2)
    print()
    c = correl(ba_closing , ko_closing)
    
    print("Correlation between BA and KO: ", c)

def correl(stock1, stock2):
    
    a = cov(stock1, stock2)
    
    b = std(stock1)
    
    c = std(stock2)
    
    d = b*c
    
    corr = a/d
    corr = np.round(corr, 2)
    
    return corr
    
def cov(stock1, stock2):
    mean1 = sum(stock1)/float(len(stock1))
    mean2 = sum(stock2)/float(len(stock2))
    
    first = [price - mean1 for price in stock1]
    sec = [price - mean2 for price in stock2]
    
    top = sum([first[i]*sec[i] for i in range(len(first))])
    
    bot = len(stock1) - 1
    
    cov = top/bot
    
    return cov

def std(stock):
    mean = sum(stock)/float(len(stock))
    
    x = [price - mean for price in stock]
    
    y = len(stock)-1
    
    num = sum([x[i]**2.0 for i in range(len(x))])
    
    
    var = (num)/y
    
    sd = var**(1/2)
    
    return sd

main()
