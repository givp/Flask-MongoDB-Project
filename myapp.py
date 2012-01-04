from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from models import *
from flaskext.bcrypt import Bcrypt
from flaskext.csrf import csrf
import logging

app = Flask(__name__)
app.config.from_object('settings')
bcrypt = Bcrypt(app)
csrf(app)

@app.route('/')
def index():
    posts = Post.objects.all()
    return render_template('index.html', p=posts)

@app.route('/record/<id>/')
def record(id):
    post = Post.objects.get(id=id)
    return render_template('record.html', p=post)

@app.route('/users/')
def users():
    users = User.objects.all()
    return render_template('users.html', u=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            this_user = User.objects.get(email=request.form['username'])
            if request.form['username'] != this_user.email:
                error = 'Invalid username'
            elif bcrypt.check_password_hash(this_user.password, request.form['password']) == False:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                session['this_user'] = {'first_name':this_user.first_name}

                flash('You were logged in')
                return redirect(url_for('index'))
        except:
            flash('User does not exist')
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
