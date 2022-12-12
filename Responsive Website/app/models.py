from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserAccount(UserMixin,db.Model):
    #for the database initialization
    #all records with relevant datatypes
    __tablename__= 'UserAccount'
    id = db.Column(db.Integer, primary_key=True)
    User = db.Column(db.String(500), index=True)  
    Email = db.Column(db.String(500), index=True)
    Password = db.Column(db.String(32), index=True)
    
    def set_password(self, Password):
        self.password_hash = generate_password_hash(Password)

    def check_password(self, Password):
        return check_password_hash(self.Password, Password)


    def is_active(self):
        return True

    def __init__(self,User,Email,Password):
        self.User = User
        self.Password= Password
        self.Email = Email
