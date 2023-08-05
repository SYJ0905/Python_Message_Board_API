import uuid
from flask import request
from flask_restful import Resource

from flask_jwt_extended import jwt_required, get_jwt_identity

from src.model.messages import Message as MessageModel
from src.model.messages import Reply as ReplyModel


class Messages(Resource):
    @jwt_required()
    def get(self):
        message_list = [
            message.to_dict() for message in MessageModel.get_message_list()
        ]
        return {"code": "1", "data": message_list, "message": "查詢所有留言成功"}


class MessageBoard(Resource):
    @jwt_required()
    def post(self):
        new_message = request.get_json()

        message = MessageModel(
            message_id=str(uuid.uuid4()).replace("-", ""),
            content=new_message.get("content"),
            create_account=get_jwt_identity(),
        )

        message.add()

        message_list = [
            message.to_dict() for message in MessageModel.get_message_list()
        ]

        return {"code": "1", "data": message_list, "message": "新增留言成功"}

    @jwt_required()
    def put(self, message_id):
        message = MessageModel.get_by_message_id(message_id)

        if message:
            temp_message = request.get_json()
            if not message.create_account == get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號更新留言"}
            else:
                message.content = temp_message.get("content")
                message.update()

            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "更新留言成功"}

        message_list = [
            message.to_dict() for message in MessageModel.get_message_list()
        ]
        return {"code": "0", "data": message_list, "message": "留言不存在"}

    @jwt_required()
    def delete(self, message_id):
        message = MessageModel.get_by_message_id(message_id)

        if message:
            if not message.create_account == get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號刪除留言"}
            else:
                message.delete()

            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "刪除留言成功"}

        message_list = [
            message.to_dict() for message in MessageModel.get_message_list()
        ]
        return {"code": "0", "data": message_list, "message": "留言不存在"}
