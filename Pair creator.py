import numpy as np
import pandas as pd
import csv
import random
tweets_all=np.load("All-tweets-array.npy",allow_pickle=True)


paired_users=[]
total_length=[]

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    seesv=list(reader)

for x in range(2):
    rand=random.randint(0,total_length)
    id=seesv[rand][0]
    follows=seesv[rand][10:120]
    breaker=False
    for a in range(total_length):
        if breaker:
            break
        friend_id=seesv[a][0]
        if friend_id in follows and id in seesv[a][10:120]:
            tweets_all[rand][0]="True"
            tweets_all[a][0]="True"
            temp=[tweets_all[rand],tweets_all[a]]
            paired_users.append(temp)
            breaker=True

for x in range(2):
    rand=random.randint(0,total_length)
    id=seesv[rand][0]
    follows=seesv[rand][10:120]
    rand2=random.randint(0,total_length)
    friends_id=seesv[rand2][0]
    if friend_id in follows and id in seesv[rand2][10:120]:
        tweets_all[rand][0]="True"
        tweets_all[a][0]="True"
    else:
        tweets_all[rand][0]="False"
        tweets_all[a][0]="False"    
    temp=[tweets_all[rand],tweets_all[a]]
    paired_users.append(temp)

np.save("All-tweets-paired-array",paired_users, allow_pickle=True) 
