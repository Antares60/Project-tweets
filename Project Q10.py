"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

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
    y=0
    score=0
    import re
    list_year=dict()
    
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
        score=0
        for word in tweet_tokens:
            if word not in stopwords:
                if word in positive_words:
                    score+=1
                elif word in negative_words:
                    score-=1
                    
        y=line.find(';')
        year=line[y:y+11]
        year=year[7:11]
        if year!= "":
            list_year[year]=list_year.get(year, 0)+score
            
    print("The sentiment score per is ", list_year)
    
except:
    print("Your file may not be in the file or you inputed the wrong file.")
    
