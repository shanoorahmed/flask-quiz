from flask import Blueprint, render_template, redirect, url_for, flash, request
from maths.extensions import db
from flask_login import login_user,logout_user, login_required
from werkzeug.security import check_password_hash
from maths.models import User
import random

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Successful!", category="success")
            return redirect(url_for('main.index'))
        else:
            flash("Invalid username or password! Please try again.", category="danger")
            return redirect(url_for('auth.login'))
            
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        unhashed_password = request.form['password']
        confirm_password = request.form['confirmpassword']
        college = request.form['college']
        year = request.form['year']

        if confirm_password != unhashed_password:
            flash("Password do not match!", category="danger")
            return redirect(url_for('auth.register'))

        user_email = User.query.filter_by(email=email).first()

        if user_email:
            flash("Email already exists!", category="danger")
            return redirect(url_for('auth.register'))

        user_username = User.query.filter_by(username=username).first()

        if user_username:
            flash("Username already exists!", category="danger")
            return redirect(url_for('auth.register'))

        easyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        midList = [11, 12, 13, 14, 15, 16]
        hardList = [17, 18, 19, 20]
        random.shuffle(easyList)
        random.shuffle(midList)
        random.shuffle(hardList)

        user = User(
            firstname=firstname,
            lastname=lastname,
            username=username, 
            email=email, 
            unhashed_password=unhashed_password, 
            college=college, 
            year=year,
            first_question = easyList[0],
            second_question = easyList[1],
            third_question = easyList[2],
            fourth_question = easyList[3],
            fifth_question = easyList[4],
            sixth_question = easyList[5],
            seventh_question = easyList[6],
            eighth_question = easyList[7],
            ninth_question = easyList[8],
            tenth_question = easyList[9],
            eleventh_question = midList[0],
            twelfth_question = midList[1],
            thirteenth_question = midList[2],
            fourteenth_question = midList[3],
            fifteenth_question = midList[4],
            sixteenth_question = midList[5],
            seventeenth_question = hardList[0],
            eighteenth_question = hardList[1],
            nineteenth_question = hardList[2],
            twentieth_question = hardList[3]
        )

        db.session.add(user)
        db.session.commit()
        flash("Registration Successful!", category="success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out!", category="warning")
    return redirect(url_for('main.index'))