import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY =os.environ.get('NEWS_API_KEY')
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=keyword&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgresql://cbcldllgjvprjb:e2901e5e72d6c578722b4b4e1826c9825d277c7bb2763fd6d17106c802b1bda4@ec2-44-193-228-249.compute-1.amazonaws.com:5432/d7djiapusrdeer?sslmode=require"

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
