from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is supposed to be secret'
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form = form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    return render_template('signup.html', form = form)


@app.route('/studyrooms')
def studyrooms():
    return render_template('table.html')



if __name__ == '_main_':
    app.run()
