import snscrape.twitter as sntwitter
import numpy as np
import pandas as pd
import csv
def scrape_twitter(name,num):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    global tweets_all
    tweets_all=[]
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{name}').get_items()):
        try:
            tweets=tweet.rawContent
        except:
            pass
        if i>99 or tweets=="":
            break
        tweets_all.append=([tweets])
    return(tweets_all)