from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.errorhandler(404)
def fourOwfour(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404