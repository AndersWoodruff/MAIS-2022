import numpy as np
import pandas as pd
import csv
import random
tweets_all=np.load("All_tweets_array.npy",allow_pickle=True)


paired_users=[][2][101]
with open("data.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    seesv=list(reader)



for x in range(1500):
    rand=random.int()
    id=seesv[rand][0]
    follows=seesv[rand][10:120]
    breaker=False
    for a in range[40000]:
        if breaker:
            break
        friend_id=seesv[a][0]
        if friend_id in follows and id in seesv[a][10:120]:
            tweets_all[rand][0]=True
            tweets_all[a][0]=True
            temp=[tweets_all[rand],tweets_all[a]]
            paired_users.append(temp)
            breaker=True

for x in range(10000):
    rand=random.int()
    id=seesv[rand][0]
    follows=seesv[rand][10:120]
    rand2=random.int()
    friends_id=seesv[rand2][0]
    if friend_id in follows and id in seesv[rand2][10:120]:
        tweets_all[rand][0]="True"
        tweets_all[a][0]="True"
    else:
        tweets_all[rand][0]="False"
        tweets_all[a][0]="False"    
    temp=[tweets_all[rand],tweets_all[a]]
    paired_users.append(temp)

np.save("All-tweets-array",paired_users, allow_pickle=True) 