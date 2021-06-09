import urllib.request,json
from .models import Source,Article
import requests
import os

apiKeyy = None
source_url = None
article_url = None
base_url =None
base_article_url = None

def configure_request(app):
    global apiKey,source_url, base_article_url
    apiKey = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    base_article_url = app.config['ARTICLES_API_BASE_URL']


def getSources():
    
    getSourcesURL = source_url.format(apiKey)
    getSourcesResponse =requests.get(getSourcesURL).json()

    sourcesResults = None 

    if getSourcesResponse['sources']:
        sourcesResultsList = getSourcesResponse['sources']
        sourcesResults = processSources(sourcesResultsList)

    return sourcesResults        

def processSources(sourceLists):
    sourcesResults = []
    for sourceList in sourceLists:
        id = sourceList.get('id')
        name = sourceList.get('name')
        description = sourceList.get('description')
        url = sourceList.get('url')
        category = sourceList.get('category')
        language = sourceList.get('language')
        country = sourceList.get('country')

        sourceObject = Source(id,name,description,url,language,category,country)

        sourcesResults.append(sourceObject)

    return sourcesResults

def get_articles(category):
    """
    Function that gets the json Articles response to our url request
    """
    get_articles_url = base_article_url.format(category, apiKey)
    get_articles_response = requests.get(get_articles_url).json()

    articles_results = None

    if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_articles_results(articles_results_list)

    return articles_results
