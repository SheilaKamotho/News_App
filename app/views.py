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
# @app.route('/bbc')
# def bbc():
#     newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
#     topheadlines = newsapi.get_top_headlines(sources="bbc-news")
 
#     articles = topheadlines['articles']
 
#     desc = []
#     news = []
#     img = []
 
#     for i in range(len(articles)):
#         myarticles = articles[i]
 
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
 
#     mylist = zip(news, desc, img)
 
#     return render_template('bbc.html', context=mylist)

# # @app.route('/source/<news_source>')
# # def source(news_source):

# #     '''
# #     View source page function and returns the news source page and its data
# #     '''
# #     title = 'News Source'
# #     newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
# #     sources = newsapi.get_sources()
# #     sources = sources['sources']
 
# #     name = []
# #     description = []
# #     url = []
 
# #     for i in range(len(sources)):
# #         mysources = sources[i]
 
# #         name.append(mysources['name'])
# #         description.append(mysources['description'])
# #         url.append(mysources['url'])
 
# #     mylist = zip(name, description, url)

# #     return render_template('source.html',id = news_source, title = title, context = mylist)

# @app.route('/article/<news_article>')
# def article(news_article):

#     '''
#     View article page function and returns the news article page and its data
#     '''
#     title = 'News Article'
#     newsapi = NewsApiClient(app.config['NEWS_API_KEY'])
#     topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english,the-verge, bbc-news" )
 
 
#     articles = topheadlines['articles']
    
#     desc = []
#     url = []
#     news = []
#     img = []
#     pub = []
#     auth = []
 
 
#     for i in range(len(articles)):
#         myarticles = articles[i]
 
 
#         news.append(myarticles['title'])
#         url.append(myarticles['url'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         pub.append(myarticles['publishedAt'])
#         auth.append(myarticles['author'])
 
 
 
#     mylist = zip(news, desc,url, img, pub, auth)
 
#     return render_template('article.html',id = news_article, title = title, context = mylist)