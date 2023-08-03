from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:MySQL0905@localhost:3306/message_board"
    )
    JWT_SECRET_KEY = "MESSAGE_BOARD"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=300)
