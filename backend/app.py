from flask import Flask
from views.api_v1 import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')

@app.route('/')
def hello():
    return "Hello world!"