from flask import Flask, render_template, flash, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import LoginForm, RegisterForm, UpdateAccountForm
from application.models import User, Post, StudyRoom
from flask_login import login_user, current_user, logout_user, login_required


@app.before_first_request
def setup_db():
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Incorrect username or password', 'danger')
    return render_template('login.html', form=form)


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/studyrooms')
@login_required
def studyrooms():


    return render_template('table.html', rooms=StudyRoom.query.all() )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated successfully', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', form=form)



@app.route('/calendar', methods=['POST', 'GET'])
@login_required
def calendar():

    return render_template('calendar.html')
