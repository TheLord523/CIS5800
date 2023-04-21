#import request to get information
#flash to flash a message
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #ensures password is never stored in plain text, and that it's stored in a hash, making it more secure
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#this file is a blueprint of our application (bunch of roots/URLS defined in it)
auth = Blueprint('auth', __name__)
#this allows login to accept POST requests. By default, we can only accept POST requests,
#but by adding these 2 strings we can accept both.
@auth.route('login', methods=['GET', 'POST'])
def login():
    #accesses all of the data that was sent as a form. However, because we also have the GET METHOD
    #every refresh gets stored too.
    #data = request.form
    #print(data)
    #Logging in Users
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category= 'success')
                login_user(user, remember = True) #stored in cache
                return redirect(url_for('views.home')) #if you login, redirect you to home page
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    return render_template("login.html", user=current_user)
    #return render_template("login.html", boolean = True)
@auth.route('login-faculty', methods=['GET', 'POST'])
def login_faculty():
    #accesses all of the data that was sent as a form. However, because we also have the GET METHOD
    #every refresh gets stored too.
    #data = request.form
    #print(data)
    #Logging in Users
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category= 'success')
                login_user(user, remember = True) #stored in cache
                return redirect(url_for('views.home_faculty')) #if you login, redirect you to home page
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    return render_template("login_faculty.html", user=current_user)
    #return render_template("login.html", boolean = True)

@auth.route('/logout')
@login_required
def logout():
    #return "<p>Logout</p>"
    logout_user()
    return redirect(url_for('auth.login')) #redirect them back to sign-in page after logging out

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category = 'error')
        #if length of email is less than 4 characters
        elif len(email) < 4:
            flash('Email must be more than 3 characters.', category ='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, firstName=firstName, password = generate_password_hash(password1, method = 'sha256') ) #hashing algorithm
            db.session.add(new_user)
            db.session.commit()
            #login_user(user, remember = True)
            #add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html", user=current_user)

@auth.route('/sign-up-faculty', methods=['GET', 'POST'])
def sign_up_faculty():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category = 'error')
        #if length of email is less than 4 characters
        elif len(email) < 4:
            flash('Email must be more than 3 characters.', category ='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            user = User(email=email, firstName=firstName, password = generate_password_hash(password1, method = 'sha256') ) #hashing algorithm
            db.session.add(user)
            db.session.commit()
            #login_user(user, remember = True)
            login_user(user, remember = True)
            #add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home_faculty'))
    return render_template("signup_faculty.html", user=current_user)

@auth.route('/home-faculty', methods=['GET', 'POST'])
def home_faculty():
    return render_template("home_faculty.html", user=current_user)

@auth.route('/view-courses', methods=['GET', 'POST'])
def view_courses():
    return render_template("view_courses.html", user=current_user)