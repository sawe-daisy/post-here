import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_URL ='http://quotes.stormconsultancy.co.uk/quotes.json'

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig
}