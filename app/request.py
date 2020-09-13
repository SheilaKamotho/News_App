from app import app
import urllib.request,json
from .models import article,source
from newsapi import NewsApiClient

Article = article.Article
Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

sources = api_key.get_sources()
all_articles = api_key.get_everything(q='bitcoin',sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',from_param='2017-12-01',to='2017-12-12',language='en',sort_by='relevancy',page=2)
