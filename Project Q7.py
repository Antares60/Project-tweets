"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input,"r", encoding="utf8")
    stopword=open("stop-words.txt","r")
    negative_word = open("negative-words.txt","r")
    postive_word = open("positive-words.txt","r")
    
    
    postive_words=[]
    for word in postive_word :
        postive_words.append(word.replace("\n",""))
        
        
    stopwords=[]
    for word in stopword:
        stopwords.append(word.replace("\n",""))
    stopwords.append('amp')
    
    negative_words=[]
    for word in negative_word :
        negative_words.append(word.replace("\n",""))
    
    x=0
    fltr =['sars cov','covid']
    
    tweet_list=[]
    import re
    list_word=dict()
    Apos_dict={"'s":" is","n't":" not","'m":" am","'ll":" will","'d":" would","'ve":" have","'re":" are"}
    
    for line in tweets:
        x=line.find(';')
        tweet=line[:x]
        tweet = re.sub(r'https?:\/\/.\S+', "", tweet)
        tweet = re.sub(r'^rt[\s]+', '', tweet)
        tweet=re.sub(r'[^\w\s]', "",tweet)
        tweet = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",tweet) if s])
        tweet=tweet.lower()
        for word in fltr :
            if word in tweet :
                tweet_tokens = tweet.split()
                for word in tweet_tokens:
                    if word not in stopwords:
                        list_word[word]=list_word.get(word, 0)+1
          
    
    pos = []
    neg = []
    contxt = []
    
    for k,v in list_word.items():
        if k not in negative_words and  k not in postive_words :
            contxt.append((v,k))
        if k in postive_words :
            pos.append((v,k))
        if k in negative_words :
            neg.append((v,k))
    
    contxt = sorted(contxt, reverse=True)
    pos = sorted(pos, reverse=True)
    neg = sorted(neg, reverse=True)
    
    temp_contxt =[]
    temp_pos =[]
    temp_neg =[]
    
    i=0
    while i<=9:
        temp_contxt.append(contxt[i])
        temp_pos.append(pos[i])
        temp_neg.append(neg[i])
        i+=1
        
        
    print ("The 10 most frequent context words are:",temp_contxt)   
    print ('') 
    print ("The 10 most frequent positive words are:",temp_pos)
    print ('')
    print ("The 10 most frequent negative words are:",temp_neg)
except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
