from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey

from src import db
from src.model.base import Base


class User(Base):
    user_id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    # password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "age": self.age,
            # "password": self.password,
            "email": self.email,
        }

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def get_by_user_id(user_id):
        return db.session.query(User).filter(User.user_id == user_id).first()

    @staticmethod
    def get_by_user_email(email):
        return db.session.query(User).filter(User.email == email).first()


class Password(Base):
    user_id = db.Column(
        db.String(64),
        ForeignKey("user.user_id", ondelete="CASCADE"),
        primary_key=True,
    )
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_user_id(user_id):
        return db.session.query(Password).filter(Password.user_id == user_id).first()
