from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Bootstrap(app)

app.config.from_object('simplewebtools.config')

db = SQLAlchemy(app)

import simplewebtools.views
