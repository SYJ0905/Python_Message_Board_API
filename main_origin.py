from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = [
    {
        "username": "Cloud",
        "age": 29,
    },
    {
        "username": "Lilias",
        "age": 30,
    },
]


@app.route("/")
def helloworld():
    return "hello world"


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(user_list)


@app.route("/user", methods=["POST"])
def create_user():
    new_user = request.get_json()
    username = new_user.get("username")

    # 检查用户名是否已存在
    for user in user_list:
        if user["username"] == username:
            return jsonify({"code": "0", "data": user_list, "message": "用戶已存在"})

    user_list.append(new_user)
    return jsonify({"code": "1", "data": user_list, "message": "新增用戶成功"})


@app.route("/user/<username>", methods=["PUT"])
def update_user(username):
    temp_user = None
    for user in user_list:
        if user["username"] == username:
            temp_user = request.get_json()
            user["age"] = temp_user["age"]

            return jsonify({"code": "1", "data": user_list, "message": "更新用戶成功"})
    if not temp_user:
        return jsonify({"code": "0", "data": user_list, "message": "用戶不存在"})


@app.route("/user/<username>", methods=["DELETE"])
def delete_user(username):
    temp_user = None
    for user in user_list:
        if user["username"] == username:
            user_list.remove(user)
            return jsonify({"code": "1", "data": user_list, "message": "刪除用戶成功"})

    if not temp_user:
        return jsonify({"code": "0", "data": user_list, "message": "用戶不存在"})


if __name__ == "__main__":
    app.run()
