from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:doanglick@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'csl87o4krjnadfcmo792'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    owner_id
    title = db.Column(db.String(220))
    entry = db.Column(db.String(2000))

    def __init__(self, title, entry):
        self.title = title
        self.entry = entry

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(220))
    password = db.Column(db.String(220))
    blogs

    def __init__(self, username):
        self.username = username

@app.before_request
def require_login():
    allowed_routes = ['login', 'list_blogs']

    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect ('/login')

@app.route('/')
def index():

@app.route('/signup')
def signup():

@app.route('/login')
def login():

def logout():



if __name__ == '__main__':
    app.run()