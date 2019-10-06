from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_blog.models

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views,entries
