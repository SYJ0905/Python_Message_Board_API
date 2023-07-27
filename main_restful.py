from flask import Flask
from flask_restful import Api

from module.resource.user import User, Users
from module.resource.hello import Helloworld

app = Flask(__name__)
api = Api(app)


api.add_resource(Helloworld, "/")

api.add_resource(Users, "/users", endpoint="users_list")
api.add_resource(User, "/user/<string:username>", endpoint="user_detail")
api.add_resource(User, "/user", endpoint="create_user")
api.add_resource(User, "/user/<string:username>", endpoint="update_user")
api.add_resource(User, "/user/<string:username>", endpoint="delete_user")

if __name__ == "__main__":
    app.run()
