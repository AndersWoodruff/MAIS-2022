import snscrape.twitter as sntwitter
import numpy as np
import pandas as pd
import csv
###(sample,tweets,tweetstats)
all_users = []
with open("data.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader:
        all_users.append(row[1])

# Creating list to append tweet data to
tweets_all=np.zeros((10000,101),dtype=object,order="C")

def scrape_twitter(name,num):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    global tweets_all
    tweets_all[num-1][0]=name
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{name}').get_items()):
        try:
            tweets=tweet.rawContent
        except:
            pass
        if i>99 or tweets=="":
            break
        tweets_all[num-1][i+1]=([tweets])

for num,name in enumerate(all_users):
    if num>200:
        break
    scrape_twitter(name,num)

np.save("All-tweets-array-2",tweets_all, allow_pickle=True)
