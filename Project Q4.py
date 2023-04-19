"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

import re

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input,"r", encoding="utf8")
    stopword=open("stop-words.txt","r")
    postive_word = open("positive-words.txt","r")
    
    stopwords=[]
    for word in stopword:
        stopwords.append(word.replace("\n",""))
    
    postive_words=[]
    for word in postive_word :
        postive_words.append(word.replace("\n",""))
    
    x=0
    
    list_word=dict()
    
    for line in tweets:
        x=line.find(';')
        tweet=line[:x]
        tweet = re.sub(r'https?:\/\/.\S+', "", tweet)
        tweet=re.sub(r'[^\w\s]', "",tweet)
        tweet = re.sub(r'^rt[\s]+', '', tweet)
        tweet = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",tweet) if s])
        tweet=tweet.lower()
        tweet_tokens=tweet.split()
        
        for word in tweet_tokens:
            if word not in stopwords:
                list_word[word]=list_word.get(word, 0)+1
          
    
    tmp=list()
    
    for k,v in list_word.items():
        if k in postive_words :
            tmp.append((v,k))
    tmp=sorted(tmp, reverse=True)
    
    print("The 50 most frequent positive words used by Donald Trump are:")
    i=0
    while i<=49:
        print([i+1], tmp[i])
        i+=1

except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
