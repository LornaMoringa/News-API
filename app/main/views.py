from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.route('/')
def index():
    
    news = getSources()

    title = 'Highlights'

    return render_template('index.html',title = title, news = news)


@main.route('/entertainment/')
def entertainment():
    
    entertainment = get_articles("entertainment")

    title = 'Entertainment'

    return render_template('entertainment.html',title = title, entertainment = entertainment)

@main.route('/business/')
def business():
    
    business = get_articles("business")

    title = 'Business'

    return render_template('business.html',title = title, business = business)



@main.route('/sports/')
def sports():
    
    sports = get_articles("sports")

    title = 'Sports'

    return render_template('sports.html',title = title, sports = sports)

@main.route('/technology/')
def technology():
    
    technology = get_articles("technology")

    title = 'Technology'

    return render_template('technology.html',title = title, technology = technology)

