import requests
# Using a GET request, Oauth and headers to retrieve information with Twitter's API
temp = requests.get('https://api.twitter.com/2/users/232891415', headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAAGvRhgEAAAAA%2BEz55naXlZ8nGNRU3vn5RmNUVec%3Dpmg235pWbZmm15NWXtgbFbJZadu00bNeZQ1hTOdW1LdquAZa8c'})
# Extracting the value of the data key from temp
data = temp.json()['data']
# Extracting username value from the value of the data key 
print(data['username'])
