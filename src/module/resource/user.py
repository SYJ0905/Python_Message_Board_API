import uuid

from flask_restful import Resource, reqparse

from flask_jwt_extended import jwt_required

from src import db

from src.model.user import User as UserModel


def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception("password required")
        if not isinstance(s, (int, str)):
            raise Exception("password format error")
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characterrs long" % min_length)

    return validate


class Users(Resource):
    @jwt_required()
    def get(self):
        # token = request.headers.get("Authorization")
        # try:
        #     jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms="HS256")
        # except jwt.ExpiredSignatureError:
        #     return {
        #         "code": "0",
        #         "data": None,
        #         "message": "Expired token. Please login to get new token",
        #     }
        # except jwt.InvalidTokenError:
        #     return {
        #         "code": "0",
        #         "data": None,
        #         "message": "Invalid token. Please register or login",
        #     }

        user_list = [user.to_dict() for user in db.session.query(UserModel).all()]
        return {
            "code": "1",
            "data": user_list,
            "message": "查詢所有用戶成功",
        }


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="username required")
    parser.add_argument("age", type=int, required=True, help="age required")
    parser.add_argument("email", type=str, required=True, help="email required")
    parser.add_argument(
        "password", type=min_length_str(5), required=True, help="password: {error_msg}"
    )

    @jwt_required()
    def get(self, id):
        user = db.session.query(UserModel).filter(UserModel.id == id).first()

        if user:
            return {"code": "1", "data": user.to_dict(), "message": "查詢用戶資料成功"}

        return {"code": "0", "data": None, "message": "用戶不存在"}

    @jwt_required()
    def post(self):
        data = User.parser.parse_args()
        email = data.email

        user = db.session.query(UserModel).filter(UserModel.email == email).first()

        if user:
            user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
            return {
                "code": "0",
                "data": user_list,
                "message": "用戶已存在",
            }

        user = UserModel(
            id=str(uuid.uuid4()).replace("-", ""),
            username=data.username,
            age=data.age,
            email=data.email,
        )
        user.set_password(data.password)

        db.session.add(user)
        db.session.commit()

        user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
        return {
            "code": "1",
            "data": user_list,
            "message": "新增用戶成功",
        }

    @jwt_required()
    def put(self, id):
        user = db.session.query(UserModel).filter(UserModel.id == id).first()

        if user:
            data = User.parser.parse_args()
            user.age = data.age
            user.email = data.email
            db.session.commit()

            user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
            return {
                "code": "1",
                "data": user_list,
                "message": "更新用戶成功",
            }

        user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
        return {
            "code": "0",
            "data": user_list,
            "message": "用戶不存在",
        }

    @jwt_required()
    def delete(self, id):
        user = db.session.query(UserModel).filter(UserModel.id == id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
            return {
                "code": "1",
                "data": user_list,
                "message": "刪除用戶成功",
            }

        user_list = [u.to_dict() for u in db.session.query(UserModel).all()]
        return {
            "code": "0",
            "data": user_list,
            "message": "用戶不存在",
        }
