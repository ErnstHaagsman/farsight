import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.api_v1 import api

app = Flask(__name__)

try:
    database_uri = os.environ['DATABASE_URI']
except KeyError:
    print("Please set the DATABASE_URI environment variable")
    exit(1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = SQLAlchemy(app)

app.register_blueprint(api, url_prefix='/api/v1')

@app.route('/')
def hello():
    return "Hello world!"