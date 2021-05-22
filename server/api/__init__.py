from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

db = SQLAlchemy(app)
