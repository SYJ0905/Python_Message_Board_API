from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

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


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="email required")
    parser.add_argument(
        "password",
        type=min_length_str(5),
        required=True,
        help="password: {error_msg}",
    )

    def post(self):
        data = Login.parser.parse_args()
        user = db.session.query(UserModel).filter(UserModel.email == data.email).first()
        if user:
            if not user.check_password(data.password):
                return {
                    "code": "0",
                    "data": None,
                    "message": "密碼錯誤",
                }
            return {
                "code": "1",
                "data": {
                    "email": user.email,
                    "token": create_access_token(identity=user.email),
                },
                "message": "登入成功",
            }
        return {
            "code": "0",
            "data": None,
            "message": "帳號不存在",
        }
