from flask import Flask
import classifier, vector_processing

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb')) # load saved model

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

if __name__ == '__main__':
   app.run()