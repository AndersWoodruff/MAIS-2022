import pandas as pd

df = pd.read_csv('twitterFriends.csv')

followersArr = []

# Making array of the number of followers of each user
for row in df.iterrows():
    followersArr.append(row)

# Determining the largest number of followers one Twitter user has
followerMax = 0
for followerCount in followersArr:
    if followerCount > followerMax:
        followerMax = followerCount

# Deleting unecessary columns from dataframe
df.drop(['screenName', 'tags', 'avatar', 'followersCount', 'friendsCount', 'lang', 'lastSeen', 'tweetId'], axis=1)

friendPairs = {}

for row in df.iterrows():
    if row == 1:
        pass
    else:
        mainId = ['id'].iat[row]
        for column in df:
            if column == 0:
                pass
            else:
                for row in df.iterrows():
                    if row == 1:
                        pass
                    else:
                        
                tempIdValue = df.iloc[row, column]
                if tempIdValue.equals(mainId):
                
