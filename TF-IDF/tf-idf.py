import pandas as pd
import sklearn as sk
import math 
from wordcloud import WordCloud

def computeTF(wordDict, doc):
    tfDict = {}
    corpusCount = len(doc)
    for word, count in wordDict.items():
        tfDict[word] = count/float(corpusCount)
    return(tfDict)

def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                if word in idfDict:
                    idfDict[word] += 1
                else:
                    idfDict[word] = 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

import os
files = os.scandir('data/')

worddicts = []
tfs = []
for f in files:
    first = []
    fname = f.name
    print(fname)
    
    txt = open('data/'+fname).read()
    txt = txt.lower() #getting text from html document and converting it to lower case
    word_freq = WordCloud().process_text(txt)
    #print(word_freq)
    
    mx = max(zip(word_freq.values(), word_freq.keys()))
    first.append(mx[1])
    
    word_freq[mx[1]] = -1
    
    mx = max(zip(word_freq.values(), word_freq.keys()))
    first.append(mx[1])
    total= set(first)
    print(total)

    wordDict = dict.fromkeys(total, 0) 
    for word in first:
        wordDict[word]+=1
        
    tf = computeTF(wordDict, first)
    worddicts.append(wordDict)
    tfs.append(tf)
    
    
print('\n\n\n')    
idfs = computeIDF(worddicts)

idfs2 = []
for tf in tfs:
    idf = computeTFIDF(tf, idfs)
    idfs2.append(idf)

idf= pd.DataFrame(idfs2)
idf=idf.fillna(0)
print(idf)


