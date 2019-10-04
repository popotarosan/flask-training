# dbはSQLAlchemyのインスタンス
from flask_blog import db
# 投稿日時を扱うので
from datetime import datetime


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),unique=True)
    text =db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    # コンストラクタ
    def __init__(self,title=None,text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    # モデルが参照された時のコンソールでの出力形式の指定
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id,self.title,self.text)