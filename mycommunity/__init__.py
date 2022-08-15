from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = '50ef59056578f21b0daf78ca4d7b823e'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

from mycommunity import routes