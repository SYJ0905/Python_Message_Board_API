from werkzeug.security import generate_password_hash, check_password_hash

from src import db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)

    # def __repr__(self):
    #     return f"id={self.id}, username={self.username}, email={self.email}, password={self.password}"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "age": self.age,
            "password": self.password,
            "email": self.email,
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def get_by_user_id(id):
        return db.session.query(User).filter(User.id == id).first()

    @staticmethod
    def get_by_user_email(email):
        return db.session.query(User).filter(User.email == email).first()
