from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thiago'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)