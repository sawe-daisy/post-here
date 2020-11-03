import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='~3og3YXm)#([yG@)I}La7(r1>fQ&7>'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # DEBUG=True
    # MAIL_USE_SSL =True
    MAIL_USE_TLS = True
    MAIL_MAX_EMAILS=None
    MAIL_ASCII_ATTACHMENTS = False
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/blogs'
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}