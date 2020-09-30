import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'
    
    DEBUG = True
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog_test'

    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

