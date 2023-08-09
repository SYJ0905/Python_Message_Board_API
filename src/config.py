from datetime import timedelta
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "MESSAGE_BOARD")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class TestingConfig(Config):
    pass


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:MySQL0905@localhost:3306/message_board"
    )
    pass


class ProductionConfig(Config):
    pass


app_config = {
    "testing": TestingConfig,
    "develop": DevelopConfig,
    "production": ProductionConfig,
}
