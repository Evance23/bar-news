from flask import render_template
from . import main
from ..request import get_news, process_results, get_articles
from ..models import Source, Article

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    #Getting the popular news list
    technology = get_news('technology')
    health = get_news('health')
    business = get_news('business')
    sports = get_news('sports')
    entertainment = get_news('entertainment')
    print(health)

    title = 'News Zone'
    return render_template('index.html',title = title,technology = technology, health = health , business= business , sports= sports , entertainment = entertainment)

@main.route('/articles/<news_id>')
def articles(news_id):
    '''
    view function that returns the source page and its data
    '''
    articles = get_articles(news_id)
    return render_template('articles.html',articles = articles) 