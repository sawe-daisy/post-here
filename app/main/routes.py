from flask import render_template
from ..models import Quotes
from . import main
from ..req import get_quotes

@main.route('/')
def index():
    quotes= get_quotes()

    return render_template('index.html', quotes=quotes)