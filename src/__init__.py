from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_jwt_extended import JWTManager

db = SQLAlchemy()

from src.module.resource.user import User, Users
from src.module.resource.message import Messages, MessageBoard, ReplyBoard

from src.module.resource.auth import Login
from src.module.resource.hello import Helloworld

from src.config import Config

jwt = JWTManager()


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return {
        "code": "0",
        "data": None,
        "message": "Missing Authorization Header",
    }, 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return {
        "code": "0",
        "data": None,
        "message": "Token has expired",
    }, 401


@jwt.invalid_token_loader
def invalid_token_callback(jwt_header):
    return {
        "code": "0",
        "data": None,
        "message": "Invalid token",
    }, 422


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(Config)
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    jwt.init_app(app)

    api.add_resource(Helloworld, "/")

    api.add_resource(Users, "/users", endpoint="users_list")
    api.add_resource(User, "/user/<string:id>", endpoint="user_detail")
    api.add_resource(User, "/user", endpoint="create_user")
    api.add_resource(User, "/user/<string:id>", endpoint="update_user")
    api.add_resource(User, "/user/<string:id>", endpoint="delete_user")

    api.add_resource(Messages, "/messages", endpoint="messages_list")
    api.add_resource(MessageBoard, "/message", endpoint="create_message")
    api.add_resource(
        MessageBoard, "/message/<string:message_id>", endpoint="update_message"
    )
    api.add_resource(
        MessageBoard, "/message/<string:message_id>", endpoint="delete_message"
    )

    api.add_resource(ReplyBoard, "/reply", endpoint="create_reply")
    api.add_resource(ReplyBoard, "/reply/<string:reply_id>", endpoint="update_reply")
    api.add_resource(ReplyBoard, "/reply/<string:reply_id>", endpoint="delete_reply")

    api.add_resource(Login, "/auth/login", endpoint="login")

    return app


# $env:FLASK_APP="src:create_app()"
# flask run
# flask db init
# flask db migrate
# flask db upgrade


# 專業級或者是服務級網路留言板具備功能:
# 註冊和登入系統：使用者可以創建帳戶並透過登入進入留言板。這樣可以管理用戶，避免未授權訪問和確保留言的來源。
# 留言發布：使用者可以撰寫和發布留言，包括文字內容、圖片、或其他媒體。
# 留言瀏覽：使用者可以瀏覽所有留言，按照不同排序方式（例如最新、熱門等）進行查看。
# 留言回覆：使用者可以對特定留言進行回覆，形成留言的回應串。
# 媒體上傳：使用者可以上傳圖片或其他媒體文件，以豐富留言內容。
# 用戶權限管理：不同用戶應該具有不同的權限，例如普通用戶、版主、管理員等，各自擁有特定的操作權限。
# 留言舉報機制：為了維護留言板的秩序，用戶可以舉報不適當的內容或垃圾留言，然後版主或管理員可以採取相應措施。
# 標籤和分類：為留言添加標籤或將留言分類，使用戶可以更容易地查找特定主題或內容。
# 搜尋功能：提供使用者進行關鍵字搜尋，以便快速找到特定內容。
# 私人訊息：使用者之間可以發送私人訊息，這有助於私下交流或討論。
# 帳戶設定：使用者可以更改個人資料、密碼、通知設定等。
# 安全性：確保網站和使用者數據的安全，防止惡意攻擊和數據洩露。


# 簡易的網路留言板具備功能:
# 留言發布：使用者可以撰寫並發布留言，包括文字內容。
# 留言瀏覽：使用者可以瀏覽所有已發布的留言，按照時間排序。
# 留言回覆：使用者可以對特定留言進行回覆，形成留言的回應串。
# 基本用戶註冊和登入：使用者可以創建帳戶並透過登入進入留言板。
# 基本用戶身份驗證：確保只有登入的使用者可以發布留言和回覆。
# 基本的安全性措施：例如避免 SQL 注入、XSS 攻擊等，確保網站的基本安全性。|
