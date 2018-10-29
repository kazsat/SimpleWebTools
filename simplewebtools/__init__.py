from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('simplewebtools.config')

db = SQLAlchemy(app)

import simplewebtools.views
