from werkzeug.security import generate_password_hash, check_password_hash

from src import db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f"id={self.id}, username={self.username}, email={self.email}, password={self.password}"

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

    # def generate_token(self):
    #     try:
    #         payload = {
    #             "exp": datetime.utcnow() + timedelta(minutes=5),
    #             "iat": datetime.utcnow(),
    #             "sub": self.email,
    #         }
    #         jwt_token = jwt.encode(
    #             payload, current_app.config.get("SECRET_KEY"), algorithm="HS256"
    #         )
    #         return jwt_token

    #     except Exception as e:
    #         return str(e)

    # @staticmethod
    # def authenticate(email, password):
    #     print("email =>", email)
    #     print("password =>", password)
    #     user = db.session.query(User).filter(User.email == email).first()
    #     if user:
    #         if user.check_password(password):
    #             print(user)
    #             return user

    # @staticmethod
    # def identity(payload):
    #     print("payload =>", payload)
    #     id = payload["identity"]
    #     user = db.session.query(User).filter(User.id == id).first()
    #     print("user =>", user)
    #     return user
