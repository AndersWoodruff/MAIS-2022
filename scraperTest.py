from TwitterIDtoUsername import getHandles
from webbrowser import Chrome
import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd


temp= getHandles([1969527638, 51878493], delayTime=0.5)

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{temp}').get_items()):
    if i>100:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

tweets_df1.to_csv(r'C:\juliawright\coding\friendFinder\my_data.csv', index=False)