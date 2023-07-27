from flask import request
from flask_restful import Resource, reqparse

user_list = [
    {"username": "Cloud", "age": 29, "password": "Cloud0905"},
    {"username": "Lilias", "age": 30, "password": "Lilias0905"},
]


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
    def get(self):
        return {"code": "1", "data": user_list, "message": "查詢所有用戶成功"}


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="username required")
    parser.add_argument("age", type=int, required=True, help="age required")
    parser.add_argument(
        "password", type=min_length_str(5), required=True, help="password: {error_msg}"
    )

    def get(self, username):
        for user in user_list:
            if user["username"] == username:
                return {"code": "1", "data": user, "message": "查詢用戶資料成功"}
        return {"code": "0", "data": None, "message": "用戶不存在"}

    def post(self):
        data = User.parser.parse_args()
        new_user = request.get_json()
        username = data.get("username")

        # 检查用户名是否已存在
        for user in user_list:
            if user["username"] == username:
                return {"code": "0", "data": user_list, "message": "用戶已存在"}

        user_list.append(new_user)
        return {"code": "1", "data": user_list, "message": "新增用戶成功"}

    def put(self, username):
        temp_user = None
        for user in user_list:
            if user["username"] == username:
                data = User.parser.parse_args()
                temp_user = request.get_json()
                user["age"] = data.get("age")
                user["password"] = data.get("password")

                return {"code": "1", "data": user_list, "message": "更新用戶成功"}
        if not temp_user:
            return {"code": "0", "data": user_list, "message": "用戶不存在"}

    def delete(self, username):
        temp_user = None
        for user in user_list:
            if user["username"] == username:
                user_list.remove(user)
                return {"code": "1", "data": user_list, "message": "刪除用戶成功"}

        if not temp_user:
            return {"code": "0", "data": user_list, "message": "用戶不存在"}
