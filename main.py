import nltk
from newspaper import Article
from textblob import TextBlob

from flask import Flask, request, render_template

# nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
  url = request.form['url']

  article = Article(url)
  article.download()
  article.parse()  
  article.nlp()

  return render_template('index.html',article=article)

if __name__ == '__main__':
    app.run(debug=True)

# https://timesofindia.indiatimes.com/city/delhi/live-news-lockdown-in-delhi-night-curfew-covid-cases-noida-gurgaon-ghaziabad-temperature-pollution-25-april-2021/liveblog/82238343.cms
