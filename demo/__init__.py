from flask import Flask
from os import environ, path
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template') 

app.config['SECRET_KEY']='5dea345b323975ede673fdc3f87c24e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/pythonproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

from demo import routes