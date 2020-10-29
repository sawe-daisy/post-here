from flask import Flask
from config import config_options
from .models import Quotes

QUOTE_URL= None

def configure_req(app):
    global QUOTE_URL
    QUOTE_URL= app.config['QUOTE_URL']
