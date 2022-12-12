from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,DateTimeField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo
import datetime

class LoginForm(FlaskForm):
    #initialize the form fields with datatypes
    userName = StringField('User Name', validators=[DataRequired()])

    userPassword = PasswordField('passwords', validators=[DataRequired()])

class SignupForm(FlaskForm):
    #initialize the form fields with datatypes
    userName = StringField('User Name', validators=[DataRequired()])
    userEmail = StringField('User Email', validators=[DataRequired()])
    userPassword = PasswordField('passwords', validators=[DataRequired()])
    userVerifyPassword = PasswordField('confirm password', validators=[DataRequired(),
                        EqualTo('userPassword')])

class changePasswords(FlaskForm):
    userEmail = StringField('User Email', validators=[DataRequired()])
    userCurrentPwd = PasswordField('Curr password', validators=[DataRequired()])
    userNewPwd = PasswordField('New password', validators=[DataRequired()])
    userVerifyNewPassword = PasswordField('confirm password', validators=[DataRequired(),
                        EqualTo('userNewPwd')])


    
def get_id(self):
    return self.userName