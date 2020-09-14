from flask import render_template
from app import app
from newsapi import NewsApiClient

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to the best News App'
    heading = 'Welcome to News App'
    
 
    return render_template('index.html', heading = heading, title = title)
@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="bbc-news")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('bbc.html', context=mylist)

@app.route('/aljeezera')
def aljeezera():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="al-jazeera-english")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('aljeezera.html', context=mylist)

@app.route('/cbc')
def cbc():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="cbc-news")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('cbc.html', context=mylist)
@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="cnn")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('cnn.html', context=mylist)

@app.route('/fortune')
def fortune():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="fortune")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('fortune.html', context=mylist)

@app.route('/medical')
def medical():
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    all_articles = newsapi.get_everything(sources="medical-news-today")
 
    articles = all_articles['articles']
    
    desc = []
    url = []
    news = []
    img = []
    pub = []
    auth = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        url.append(myarticles['url'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        pub.append(myarticles['publishedAt'])
        auth.append(myarticles['author'])
 
 
 
    mylist = zip(news, desc,url, img, pub, auth)
    return render_template('medical.html', context=mylist)

@app.route('/source')
def source():

    '''
    View source page function and returns the news source page and its data
    '''
    title = 'News Source'
    newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
    sources = newsapi.get_sources()
    sources = sources['sources']
 
    name = []
    description = []
    url = []
 
    for i in range(len(sources)):
        mysources = sources[i]
 
        name.append(mysources['name'])
        description.append(mysources['description'])
        url.append(mysources['url'])
 
    mylist = zip(name, description, url)

    return render_template('source.html', title = title, context = mylist)
    