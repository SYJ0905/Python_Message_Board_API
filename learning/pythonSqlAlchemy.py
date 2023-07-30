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


# 建立 MySQL 連線
engine = sa.create_engine("mysql+pymysql://root:MySQL0905@localhost:3306/demo")
BASE.metadata.create_all(engine)
Session = sa.orm.sessionmaker(bind=engine)
session = Session()

# 插入數據
user1 = User(username="test1", password="test1", email="test1@test1.com")
user2 = User(username="test2", password="test2", email="test2@test2.com")
user3 = User(username="test3", password="test3", email="test3@test3.com")
session.add(user1)
session.add_all([user2, user3])
session.commit()
