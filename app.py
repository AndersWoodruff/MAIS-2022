from flask import Flask, render_template, request
import classifier
import scrape_tweets
from vector_processing import get_average_vector, get_cosine_similarity
import pickle
import numpy as np

app = Flask(__name__)

classifier.train_model([[2],[3],[4],[5],[2]],[[0],[0],[0],[0],[0]]) # add training data here, right now contains test values
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
