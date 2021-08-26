from datetime import datetime

from app01 import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    loginid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    isdelete = db.Column(db.Boolean, default=False)
    rdate = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username
