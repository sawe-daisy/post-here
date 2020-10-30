import urllib.request, json
from config import config_options
from .models import Quotes

QUOTE_URL= None

def configure_req(app):
    global QUOTE_URL
    QUOTE_URL= app.config['QUOTE_URL']


def get_quotes():
    
    with urllib.request.urlopen(QUOTE_URL) as url:
        quotes_data= url.read()
        quotes_response=json.loads(quotes_data)
        # import pdb; pdb.set_trace()
        # get_quotes_list= []
        # if quotes_response['quote']:
        get_quotes_list=process_results(quotes_response)

    return get_quotes_list

def process_results(results):
    process=[]
    for item in results:
        author = item.get('author')
        quote=item.get('quote')
        permalink=item.get('permalink')

        if quote:
            new_quote=Quotes(author, quote, permalink)
            process.append(new_quote)

    return process    