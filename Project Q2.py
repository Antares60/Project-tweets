# -*- coding: utf-8 -*-
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
        date=line[x:x+11]
        date=date[7:11]
        if date!= "":
            list_date[date]=list_date.get(date, 0)+1
                
    print(list_date)

except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
