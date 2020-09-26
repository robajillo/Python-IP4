
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/blog'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True
    


