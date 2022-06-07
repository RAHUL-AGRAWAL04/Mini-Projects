from bs4 import BeautifulSoup
from wordcloud import WordCloud
import os
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#ps.stem(word)

path = '/home/kali/Desktop/inverted index/data'
files = os.scandir(path)

ii = {}
#ii = {word:{file_name:freq}}

for f in files:
    html = open(path+f.name).read()
    soup = BeautifulSoup(html)
    txt = (soup.get_text()).lower() #getting text from html document and converting it to lower case
    word_freq = WordCloud().process_text(txt)
    #print(type(word_freq))
    
    for t,freq in word_freq.items():
        token = ps.stem(t) #Handelling root words
        if token in ii:
            try:
                ii[token][f.name] += freq
            except:
                d = ii[token]
                d[f.name] = freq
                ii[token] = d
        else:
            ii[token] = {f.name:freq}
            
    #print(ii)

        
import json

with open('iverted_index.json', 'w') as fp:
    json.dump(ii, fp)


search = True
print('\n\n')

while search:
    merged = {}
    key_word = input('\nEnter one/multiple word to search["exit" to exit]:').strip().split()
    if len(key_word)>=2:
        flag = str(input('Combined word search [True/False]: '))
    else:flag = str(False)
    if key_word[0].lower() == 'exit':
        break
    else:
        for k in key_word:
            try:
                key = ps.stem(k)
                indexes = []
                for k,v in ii[key].items():
                    indexes.append((k,v,key))
                indexes.sort(key = lambda x:x[1], reverse = True)
                merged[key]=indexes
                print('\n\nfor root word - '+key)
                print('------------------------------ + ------------------------------')
                print('{:30} | {:30}'.format('file_name','frequency'))
                print('------------------------------ + ------------------------------')
                for e in indexes:
                    print('{:30} | {:30}'.format(e[0],str(e[1])))
            except: print('[-] failed to search')
        
        #print('\n',len(merged),str(flag),'\n')
        if(len(merged)>=2 and flag==str(True)):
            lis=[]
            for k,v in merged.items():
                lis=lis+v
            res=[]
            for i in lis:
                temp=[i[0],i[1]]
                for j in lis:
                    if(i[2]==j[2]):
                        continue
                    elif(i[0]==j[0]):                        
                        temp[1]+=j[1]
                if(temp not in res):
                    res.append(temp)
            res.sort(key = lambda x:x[1], reverse = True)
            print('\n\nfor combined root word - ')
            print('------------------------------ + ------------------------------')
            print('{:30} | {:30}'.format('file_name','frequency'))
            print('------------------------------ + ------------------------------')
            for e in res:
                print('{:30} | {:30}'.format(e[0],str(e[1])))

                
    
