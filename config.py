import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
class ProdConfig(Config):
    DATABASE_URL = 'postgres://uttqoetiuwdjyr:8232fad3955e3137ef7a0d96470eaf1fee7e1e4aa20422ff040f96f85cbb67d6@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dc9df4caacephi'

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'
    
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog_test'

    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

