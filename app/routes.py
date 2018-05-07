from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app import db, app
from app.models import User
from app.mongoland import MongoLord
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
@login_required
def index():
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
    log = MongoLord()
    time = datetime.utcnow()
    log.mongo_logging(request.method, request.endpoint,
                      request.url, time)
    return render_template('index.html', title='World', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    log = MongoLord()
    time = datetime.utcnow()
    if form.validate_on_submit():
        log.mongo_logging(request.method, request.endpoint,
                          request.url, time)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    log.mongo_logging(request.method, request.endpoint,
                      request.url, time)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats!! You are registered!! ')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
