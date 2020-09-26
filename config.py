import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    
class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

