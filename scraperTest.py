import snscrape.twitter as sntwitter
import numpy as np
import pandas as pd
import csv
###(sample,tweets,tweetstats)
all_users = []
"""with open("data.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader:
        all_users.append(row[1])"""

# Creating list to append tweet data to
tweets_all=np.zeros((4,100,2),dtype=object,order="C")
print(tweets_all)
def scrape_twitter(name,num):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    global tweets_all
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{name}').get_items()):
        if i>100 or tweet.content=="":
            break
        tweets_all[num-1,][i-1]=([tweet.content, tweet.user.username])

for num,name in enumerate(['Mixed_Lib']):
    scrape_twitter(name,num)

print(tweets_all)
# Creating a dataframe from the tweets list above 
#tweets_df1 = pd.DataFrame(tweets_list1, columns=[ 'Text', 'Username'])

#tweets_df1.to_csv(r'C:\juliawright\coding\friendFinder\my_data.csv', index=False)
