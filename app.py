from flask import Flask
import classifier, vector_processing

app = Flask(__name__)

# to test web app
@app.route('/')
def index():
   print('Request for index page received')
   return 'index.html'

if __name__ == '__main__':
   app.run()