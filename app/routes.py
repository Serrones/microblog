from flask import render_template, flash, redirect, request, url_for
from datetime import datetime
from app import app
from app.mongoland import MongoLord
from app.forms import LoginForm

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
    log_info = {"method": request.method,
                "endpoint": request.endpoint,
                "url": request.url,
                "data": datetime.utcnow()
             }

    log = MongoLord()
    log.mongo_logging(log_info)
    return render_template('index.html', title='World', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
                                    form.username.data, form.remember_me.data))
        log_info = {"method": request.method,
                    "endpoint": request.endpoint,
                    "url": request.url,
                    "data": datetime.utcnow()
                 }
        log = MongoLord()
        log.mongo_logging(log_info)
        return redirect(url_for('index'))
    log_info = {"method": request.method,
                "endpoint": request.endpoint,
                "url": request.url,
                "data": datetime.utcnow()
             }
    log = MongoLord()
    log.mongo_logging(log_info)
    return render_template('login.html', title='Sign In', form=form)
