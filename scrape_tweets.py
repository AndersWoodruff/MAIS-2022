from snscrape.modules import twitter as sntwitter
import numpy as np
import pandas as pd
import csv

def scrape_twitter(name):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    tweets_all=[]
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{name}').get_items()):
        try:
            tweets=tweet.rawContent
        except:
            pass
        if i>99 or tweets=="":
            break
        tweets_all.append(tweets)
    return(tweets_all)