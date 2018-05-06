from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
app.config['MONGO_DBNAME'] = Config.MONGO_DBNAME
app.config['MONGO_URI'] = Config.MONGO_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mongo = PyMongo(app)

from app import routes, models
