from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")

if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "App is working successfully!"
