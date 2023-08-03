import uuid
from flask import request
from flask_restful import Resource

from flask_jwt_extended import jwt_required

from src import db

from src.model.messages import Message as MessageModel
from src.model.messages import Reply as ReplyModel


class Messages(Resource):
    @jwt_required()
    def get(self):
        message_list = [
            message.to_dict() for message in db.session.query(MessageModel).all()
        ]
        return {"code": "1", "data": message_list, "message": "查詢所有留言成功"}


class MessageBoard(Resource):
    @jwt_required()
    def post(self):
        new_message = request.get_json()
        print("new_message =>", new_message)

        message = MessageModel(
            message_id=str(uuid.uuid4()).replace("-", ""),
            content=new_message.get("content"),
        )

        db.session.add(message)
        db.session.commit()

        message_list = [
            message.to_dict() for message in db.session.query(MessageModel).all()
        ]

        return {"code": "1", "data": message_list, "message": "新增留言成功"}

    @jwt_required()
    def put(self, message_id):
        message = (
            db.session.query(MessageModel)
            .filter(MessageModel.message_id == message_id)
            .first()
        )

        if message:
            temp_message = request.get_json()
            message.content = temp_message.get("content")
            db.session.commit()

            message_list = [
                message.to_dict() for message in db.session.query(MessageModel).all()
            ]
            return {"code": "1", "data": message_list, "message": "更新留言成功"}

        message_list = [
            message.to_dict() for message in db.session.query(MessageModel).all()
        ]
        return {"code": "0", "data": message_list, "message": "留言不存在"}

    @jwt_required()
    def delete(self, message_id):
        message = (
            db.session.query(MessageModel)
            .filter(MessageModel.message_id == message_id)
            .first()
        )

        if message:
            db.session.delete(message)
            db.session.commit()

            message_list = [
                message.to_dict() for message in db.session.query(MessageModel).all()
            ]
            return {"code": "1", "data": message_list, "message": "刪除留言成功"}

        message_list = [
            message.to_dict() for message in db.session.query(MessageModel).all()
        ]
        return {"code": "0", "data": message_list, "message": "留言不存在"}
