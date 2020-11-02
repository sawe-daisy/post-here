import urllib.request, json
from config import config_options
from .models import Quotes
import requests


QUOTE_URL= None

def configure_req(app):
    global QUOTE_URL
    QUOTE_URL= app.config['QUOTE_URL']


def get_quotes():
    
    get_response= requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    return get_response
