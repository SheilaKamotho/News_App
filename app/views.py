from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    heading = 'Welcome to News App'
    return render_template('index.html', heading = heading)

@app.route('/source/<news_source>')
def source(news_source):

    '''
    View source page function and returns the news source page and its data
    '''
    return render_template('source.html',id = news_source)

@app.route('/article/<news_article>')
def article(news_article):

    '''
    View article page function and returns the news article page and its data
    '''
    return render_template('article.html',id = news_article)