from flask import Flask, render_template, request
import classifier
import scrape_tweets
from vector_processing import get_average_vector, get_cosine_similarity
import pickle
import numpy as np

app = Flask(__name__)

tweets_all=np.load("All-tweets-paired-array.npy",allow_pickle=True)

labels = []
data = []

for pair in tweets_all:
   labels.append(pair[0][0])
   user_a_tweets = [pair[0][x][0] for x in range(1, len(pair[0]))]
   user_b_tweets = [pair[1][x][0] for x in range(1, len(pair[1]))]
   data.append(get_cosine_similarity(get_average_vector(user_a_tweets), get_average_vector(user_b_tweets)))

classifier.train_model(data,labels) # add training data here, right now contains test values
model = pickle.load(open('model.pkl','rb')) # load saved model

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/predictFromForm',methods=['POST'])
def predictFromForm():
   # get usernames from user input and store in data
   usernames = [str(x) for x in request.form.values()] ## gets all inputs from POST rest API call  
   print(usernames)

   # scrape last 100 tweets of each user
   tweet_data_1 = scrape_tweets.scrape_twitter(usernames[0])
   tweet_data_2 = scrape_tweets.scrape_twitter(usernames[1])
   
   # get average vector for each user
   user1_avg = get_average_vector(tweet_data_1) # use values from scrape (previous step)
   user2_avg = get_average_vector(tweet_data_2)

   # get the cosine similarity based on above step
   cos_sim_users = get_cosine_similarity(user1_avg,user2_avg) 
   # cos_sim_users = get_cosine_similarity([1, 3, 5],[4, 2, 2]) # values for testing

   # predict whether they'll be friends or not!
   prediction = classifier.make_prediction(model,[cos_sim_users])
   print(prediction)
   if prediction == 0:
      prediction = "unlikely"
   else:
      prediction = "likely"

   return render_template('index.html', predictionText='These two users are {} to be friends!'.format(prediction))

if __name__ == '__main__':
   app.run()
