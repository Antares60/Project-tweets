"""
@author: BIMONT Antoine, MIU Radu, RODYCH Vladislav, YE Michel 
"""

#file name is trump_tweets.txt
try:
    Input=input("Input file name: ")
    tweets=open(Input, 'r', encoding="utf8")
    x=0
    for line in tweets:
        x=line.find(';')
        year=line[x:x+11]
        year=year[7:11]
        if year!= "":
            print(year)
except:
    print("Your file may not be in the right folder or you inputed the wrong file.")
