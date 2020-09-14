import urllib.request,json
from .models import Article,Source


# Getting api key
api_key = None

# Getting the movie base url
base_url = None

# all_articles = api_key.get_everything(sort_by='source')

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
