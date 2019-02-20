
from flask import render_template
from app import app
from .request import get_source,get_article

@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    General_category=get_source("general")
    Business_category=get_source("business")
    Sports_category=get_source("sports")
    Entertainment_category=get_source("entertainment")
    Technology_category=get_source("technology")

    title='News Highlight Website'
    return render_template('index.html',title=title,general=General_category,business=Business_category,sports=Sports_category,entertainment=Entertainment_category,technology=Technology_category)

@app.route('/article/<id>')
def article(id):
    '''
    View source page function that returns the article details page and its data
    '''
    article=get_article(id)
    print(article)
    title= " Articles"
    return render_template('article.html',title=title, article = article )
