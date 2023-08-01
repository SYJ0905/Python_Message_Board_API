import uuid
from flask import request
from flask_restful import Resource

# MySQL 套件
# import sqlalchemy as sa
# from sqlalchemy.orm import declarative_base, relationship

# BASE = declarative_base()

messages = [
    # {
    #     "id": str(uuid.uuid4()).replace("-", ""),
    #     "content": "content",
    #     "replies": [
    #         {
    #             "id": str(uuid.uuid4()).replace("-", ""),
    #             "content": "content",
    #         }
    #     ],
    # }
]


# class Message(BASE):
#     __tablename__ = "message"

#     id = sa.Column(sa.String(36), primary_key=True)
#     content = sa.Column(sa.String(200), nullable=False)
#     create_at = sa.Column(sa.DateTime, server_default=sa.func.now())
#     replies = relationship("Reply", back_populates="message")


# class Reply(BASE):
#     __tablename__ = "reply"

#     id = sa.Column(sa.String(36), primary_key=True)
#     content = sa.Column(sa.String(200), nullable=False)
#     create_at = sa.Column(sa.DateTime, server_default=sa.func.now())
#     message_id = sa.Column(sa.String(36), sa.ForeignKey("message.id"))
#     message = relationship("Message", back_populates="replies")


class Messages(Resource):
    def get(self):
        return {"code": "1", "data": messages, "message": "查詢所有留言成功"}


class MessageBoard(Resource):
    def post(self):
        new_message = request.get_json()

        new_message["id"] = str(uuid.uuid4()).replace("-", "")
        # new_message["replies"] = []
        messages.append(new_message)
        return {"code": "1", "data": messages, "message": "新增留言成功"}

    def put(self, id):
        temp_message = None
        for message in messages:
            if message["id"] == id:
                temp_message = request.get_json()
                message["content"] = temp_message.get("content")

                return {"code": "1", "data": messages, "message": "更新留言成功"}
        if not temp_message:
            return {"code": "0", "data": messages, "message": "留言不存在"}

    def delete(self, id):
        temp_message = None
        for message in messages:
            if message["id"] == id:
                messages.remove(message)
                return {"code": "1", "data": messages, "message": "刪除留言成功"}

        if not temp_message:
            return {"code": "0", "data": messages, "message": "留言不存在"}
