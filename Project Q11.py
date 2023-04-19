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
    
    negative_words=[]
    for word in negative_word :
        negative_words.append(word.replace("\n",""))
    
    x=0
    list_word = dict()
    score = 0
    
    for line in tweets:
        x=line.find(';')
        tweet=line[:x]
        tweet = re.sub(r'https?:\/\/.\S+', "", tweet)
        tweet = re.sub(r'^rt[\s]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'@', '', tweet)
        tweet=re.sub(r'[^\w\s]', "",tweet)
        tweet = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",tweet) if s])
        if tweet.startswith("RT") == False :
            tweet=tweet.lower()
            tweet = re.sub(r'rt', '', tweet)
            tweet_tokens=tweet.split()
            score = 0
            for word in tweet_tokens:
                if word not in stopwords :
                    if word in positive_words:
                        score += 1
                    elif word in negative_words :
                            score -= 1
            date=line[x:x+11]
            date = date[7:11]
            if date!= "":
                list_word[date]=list_word.get(date, 0) + score 
    
          
    
    print ("The sentiment score is:", list_word)

except:
    print("Your file may not be in the file or you inputed the wrong file.")
    
