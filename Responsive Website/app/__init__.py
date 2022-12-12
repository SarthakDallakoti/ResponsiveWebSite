from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dallakotisarthak@gmail.com'
app.config['MAIL_PASSWORD'] = 'rgybixbmhvmyydke'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


migrate = Migrate(app, db)
admin = Admin(app,template_mode='bootstrap4')

from app import views,models
