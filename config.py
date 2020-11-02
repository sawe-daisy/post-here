import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig
}