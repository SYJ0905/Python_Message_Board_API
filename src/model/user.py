from src import db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
