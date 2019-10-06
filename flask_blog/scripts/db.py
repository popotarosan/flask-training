from flask_script import Command
from flask_blog import db
# modelをきちんと読み込む必要がある？
import flask_blog.models

class InitDB(Command):
    "create datavase"

    def run(self):
        db.create_all()