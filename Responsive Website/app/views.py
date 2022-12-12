#import relevent modules
from flask import render_template, flash,redirect,request
from app import app , models,db,admin,login_manager,mail
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from .forms import LoginForm,SignupForm,changePasswords
from .models import UserAccount
from flask_login import LoginManager,login_required,logout_user,login_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message


admin.add_view(ModelView(UserAccount, db.session))

@login_manager.user_loader
def load_user(id):
    return UserAccount.query.get(int(id))

@app.route('/', methods=['GET','POST'])
# @login_required
def Homepage():
    return render_template('home.html',
                           title='HomePage')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if current_user.is_authenticated:
        return redirect('/account')
    form = LoginForm()
    user_name = form.userName.data
    if form.validate_on_submit():
        userAcc = UserAccount.query.filter_by(User = user_name).first()
        if userAcc is None or not userAcc.check_password(form.userPassword.data):
            error = 'Invalid Login'
            return redirect('/login')
        login_user(userAcc)
        return redirect('/account')
    return render_template('login.html',
                        title='Login',form = form)
@app.route('/create_account', methods=['GET','POST'])
def signup():

    form = SignupForm()
    user_name = form.userName.data
    user_email = form.userEmail.data
    user_password = form.userPassword.data
    if form.validate_on_submit():
        user_n = UserAccount.query.filter_by(User=user_name).first()
        user_e = UserAccount.query.filter_by(Email=user_email).first()
        if user_n is not None:
            flash('User already exists')
            return redirect('/create_account')
        if user_e is not None:
            flash('email ID already exists')
            return redirect('/create_account')
        # paswrd = User.set_password(form.pwd.data)
        userData = UserAccount(User =user_name,Email =user_email,Password = generate_password_hash(form.userPassword.data))
        db.session.add(userData)
        db.session.commit()
        msg = Message('Account Created', sender = 'dallakotisarthak@gmail.com', recipients = [user_email])
        msg.body = "This is the email body"
        mail.send(msg)
        login_user(userData)
        return redirect('/login')
    return render_template('signup.html',
                        title='Signup',form = form)
    
#route for user authentication
# i want to create a form where users can log in

@app.route('/account', methods=['GET','POST'])
@login_required
def Accountpage():
    return render_template('Account.html',
                           title='User Account')

@app.route('/changePassword', methods= ['GET','POST'])
def changePassword():
    form = changePasswords()
    currPassword = form.userCurrentPwd.data
    user_email = form.userEmail.data
    if form.validate_on_submit():
        userAcc = UserAccount.query.filter_by(User = current_user.User).first()
        if userAcc is None or not userAcc.check_password(currPassword):
            flash('Invalid Login')
            return redirect('/changePassword')
        userAcc.Password = generate_password_hash(form.userNewPwd.data)
        db.session.commit()
        msg = Message('Account Password Changed', sender = 'dallakotisarthak@gmail.com', recipients = [user_email])
        msg.body = "This is the email body"
        mail.send(msg)
        logout()
        return redirect('/login')
    return render_template('changePassword.html',
                    title= 'Change Password', form = form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')