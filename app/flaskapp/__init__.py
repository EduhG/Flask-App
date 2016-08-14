from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

import flaskapp.routes

app.config.from_pyfile('../config.cfg')
'''
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'
'''
from routes import mail

mail.init_app(app)


#app.config.from_pyfile('config.cfg')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mtotooh@localhost/development'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from models import db

db.init_app(app)
