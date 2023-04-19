"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

import re

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input,"r", encoding="utf8")
    stopword=open("stop-words.txt","r")
    negative_word = open("negative-words.txt","r")
    positive_word = open("positive-words.txt","r")
    
    
    positive_words=[]
    for word in positive_word :
        positive_words.append(word.replace("\n",""))
        
    
    stopwords=[]
    for word in stopword:
        stopwords.append(word.replace("\n",""))
    stopwords.append('amp')
    
    negative_words=[]
    for word in negative_word :
        negative_words.append(word.replace("\n",""))
    
    x=0
    score_positive=0
    score_negative=0
    score=0
    list_word=dict()
    
    for line in tweets:
        x=line.find(';')
        tweet=line[:x]
        tweet = re.sub(r'https?:\/\/.\S+', "", tweet)
        tweet = re.sub(r'^rt[\s]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'@', '', tweet)
        tweet=re.sub(r'[^\w\s]', "",tweet)
        tweet = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",tweet) if s])
        tweet=tweet.lower()
        tweet = re.sub(r'rt', '', tweet)
        tweet_tokens = tweet.split()    
        for word in tweet_tokens:
            if word not in stopwords:
                if word in positive_words:
                    score_positive+=1
                elif word in negative_words:
                    score_negative+=1
    
    score=score_positive-score_negative
    print("The sentiment score is ",score)

except:
    print("Your file may not be in the file or you inputed the wrong file.")
    
