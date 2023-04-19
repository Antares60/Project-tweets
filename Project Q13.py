"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

import re

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input, 'r', encoding="utf8")
    x=0 
    space=0
    amp=0
        
    list_users=dict()
    for tweet in tweets:
        tweet=re.sub(r'[^\w\s@]',' ', tweet)
        amp=tweet.find('@')
        space=tweet.find(' ', amp)
        user=tweet[amp:space]
        while amp!=-1:
            if user!= "" and user!="@":
                list_users[user]=list_users.get(user, 0)+1 
            amp=tweet.find('@', space)
            space=tweet.find(' ', amp)
            user=tweet[amp:space]
    
    tmp=[]
    
    for k,v in list_users.items():   
            tmp.append((v,k))
    tmp=sorted(tmp, reverse=True)
    
    i=0
    while i<=19:
        print([i], tmp[i])
        i+=1

except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
    
