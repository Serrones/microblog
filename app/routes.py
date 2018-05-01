from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Serrones'}
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland'
        },
        {
        'author': {'username': 'Rose'},
        'body': 'Another job done!'
        }
    ]
    return render_template('index.html', title='World', user=user, posts=posts)
