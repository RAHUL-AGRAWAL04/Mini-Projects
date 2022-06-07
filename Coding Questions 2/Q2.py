import A10_Q1 as Q1
import yfinance as yf
import numpy as np

def relstd(stock):
    mean= sum(stock)/float(len(stock))
    mean = np.round(mean, 2)
    a = Q1.std(stock)*100/mean
    #print(a,mean)
    return a

companies = {
            'Boeing' : 'ba',
            'Coca Cola' : 'ko',
            'Exxon Mobil' : 'xom',
            'General Electric' : 'ge',
            'JP Morgan' : 'jpm',
            'Nike' : 'nke',
            'Pfeizer' : 'pfe',
            'Verizon' : 'vz'   
            }

print('{:20} | {:20}'.format('Company','Relative std deviation '))
print('-------------------- + --------------------')
for key in companies:
    df  = yf.download(companies[key], start='2020-01-01', end = '2020-12-31', progress = False)
    close = df['Close']
    rel_std = relstd(close)
    print('{:20} | {:20}'.format(key,str(np.round(rel_std,2))))
    

    
