from flask import Flask
from flask_restful import Api

from module.resource.user import User, Users
from module.resource.hello import Helloworld

app = Flask(__name__)
api = Api(app)


api.add_resource(Helloworld, "/")

api.add_resource(Users, "/users", endpoint="users_list")
api.add_resource(User, "/user/<string:user_id>", endpoint="user_detail")
api.add_resource(User, "/user", endpoint="create_user")
api.add_resource(User, "/user/<string:user_id>", endpoint="update_user")
api.add_resource(User, "/user/<string:user_id>", endpoint="delete_user")

if __name__ == "__main__":
    app.run()

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
