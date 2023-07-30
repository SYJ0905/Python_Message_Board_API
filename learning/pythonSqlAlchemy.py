from datetime import datetime

# MySQL 套件
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

BASE = declarative_base()


# 定義 table 表
class User(BASE):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), unique=True)
    password = sa.Column(sa.String(64))
    email = sa.Column(sa.String(128), unique=True)
    create_at = sa.Column(sa.DateTime, server_default=sa.func.now())

    def __repr__(self):
        return f"id={self.id}, username={self.username}, email={self.email}, password={self.password}"


# 建立 MySQL 連線
engine = sa.create_engine("mysql+pymysql://root:MySQL0905@localhost:3306/demo")
BASE.metadata.create_all(engine)
Session = sa.orm.sessionmaker(bind=engine)
session = Session()

########################################################################################

# 插入數據
# user1 = User(username="test1", password="test1", email="test1@test1.com")
# user2 = User(username="test2", password="test2", email="test2@test2.com")
# user3 = User(username="test3", password="test3", email="test3@test3.com")
# session.add(user1)
# session.add_all([user2, user3])
# session.commit()

########################################################################################

# 查詢數據
# users = session.query(User)
# for u in users:
#     print("u =>", u)

# 過濾數據
# users = session.query(User).filter(User.username == "test1")
# users = session.query(User).filter(User.username.in_(["test1", "test2"]))
# users = session.query(User).filter(User.username.like("%t2"))
# for u in users:
#     print("u =>", u)

# 排序數據
# users = session.query(User).order_by(User.id.desc())
# for u in users:
#     print("u =>", u)

# 限制數據
# users = session.query(User).limit(2)
# for u in users:
#     print("u =>", u)

# 處理數據
# users = session.query(User).all()
# users = session.query(User).first()

########################################################################################

# users1 = session.query(User)
# for u in users1:
#     print("users1 =>", type(u))

# users2 = session.query(User.id, User.username)
# for u in users2:
#     print("users2 =>", type(u))

########################################################################################

# 更新數據
# users = session.query(User).filter(User.username == "test1").first()
# print(users.email)
# users.password = "test111"
# session.commit()

########################################################################################

# 刪除數據
# user_to_delete = session.query(User).filter(User.username == "test1").first()
# if user_to_delete:
#     session.delete(user_to_delete)
#     session.commit()
#     print("數據記錄已成功刪除。")
# else:
#     print("找不到要刪除的數據記錄。")

########################################################################################
