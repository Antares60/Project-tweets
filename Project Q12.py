"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input, 'r', encoding="utf8")
    x=0        
    list=[]
    list_date=dict()
    for line in tweets:
        x=line.find(';')
        date=line[x:x+14]
        date=date[12:14]
        if date!= "":
            list_date[date]=list_date.get(date, 0)+1
    
    
    H = []
    
    for k,v in list_date.items():
                H.append((v,k))
       
    H = sorted(H, reverse=True)
    
    print('Donald Trump is more active on Twitter at',int(H[0][1]),'o clock','.')
except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
    
