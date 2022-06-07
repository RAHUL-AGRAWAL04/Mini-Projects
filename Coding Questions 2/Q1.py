import yfinance as yf
import pandas as pd 
import numpy as np

def std(stock):
    mean = sum(stock)/float(len(stock))
    
    x = [price - mean for price in stock]
    
    y = len(stock)-1
    
    num = sum([x[i]**2.0 for i in range(len(x))])
    
    
    var = (num)/y
    
    sd = var**(1/2)
    
    return sd

def var(stock):
    mean = sum(stock)/float(len(stock))
    
    x = [price - mean for price in stock]
    
    y = len(stock)-1
    
    num = sum([x[i]**2.0 for i in range(len(x))])
    
    
    var = (num)/y
    
    return var
    
    

def main(): 
    print("Prgram that calculates IBM stock data stiastics for year 2020")
    
    
         
    
    ibm_df = yf.download('ibm', start = '2020-01-01', end = '2020-12-31', progress = False)
    
    mean_ibm = sum(ibm_df['Close'])/len(ibm_df['Close'])
    mean_ibm = np.round(mean_ibm, 2)
    
    ibm_close = ibm_df['Close']
    
    n = ibm_close.shape
    
    print("\nThere are ",n," rows of stock data")
    
    sd_ibm = np.round(std(ibm_close),2)

    
    var_ibm = np.round(var(ibm_close),2)
  
        
    print("\nIBM 2020 average stock value:\t", mean_ibm)
    
    print("\nIBM stock variance:\t", var_ibm)
    
    print("\nIBM stock standard deviation:\t", sd_ibm)
    
    print("\nIBM stock variance:\t", var_ibm)                       
        
    max_ibm = np.round(ibm_close.max(),2)
    
    min_ibm = np.round(ibm_close.min(),2)
    
    maxdate_ibm = ibm_close.idxmax()
    
    mindate_ibm = ibm_close.idxmin()
    
    print("\nThe max stock value ", max_ibm, "was on ", maxdate_ibm.date())
    
    print("\nThe min stock value ", min_ibm, "was on ", mindate_ibm.date())
    


#main()
