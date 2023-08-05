import uuid
from flask import request
from flask_restful import Resource

from flask_jwt_extended import jwt_required, get_jwt_identity

from src.model.messages import Message as MessageModel
from src.model.messages import Reply as ReplyModel


class Messages(Resource):
    @jwt_required()
    def get(self):
        try:
            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "查詢所有留言成功"}
        except Exception as e:
            return {"code": "0", "data": None, "message": "查詢留言失敗：" + str(e)}


class MessageBoard(Resource):
    @jwt_required()
    def post(self):
        try:
            new_message = request.get_json()
            content = new_message.get("content")

            if not content:
                return {"code": "0", "data": None, "message": "請提供留言內容"}

            message = MessageModel(
                message_id=str(uuid.uuid4()).replace("-", ""),
                content=content,
                create_account=get_jwt_identity(),
            )

            message.add()

            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "新增留言成功"}
        except Exception as e:
            return {"code": "0", "data": None, "message": "新增留言失敗：" + str(e)}

    @jwt_required()
    def put(self, message_id):
        try:
            message = MessageModel.get_by_message_id(message_id)

            if not message:
                return {"code": "0", "data": None, "message": "留言不存在"}

            temp_message = request.get_json()
            if message.create_account != get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號更新留言"}

            message.content = temp_message.get("content")
            message.update()

            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "更新留言成功"}
        except Exception as e:
            return {"code": "0", "data": None, "message": "更新留言失敗：" + str(e)}

    @jwt_required()
    def delete(self, message_id):
        try:
            message = MessageModel.get_by_message_id(message_id)

            if not message:
                return {"code": "0", "data": None, "message": "留言不存在"}

            if message.create_account != get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號刪除留言"}

            message.delete()

            message_list = [
                message.to_dict() for message in MessageModel.get_message_list()
            ]
            return {"code": "1", "data": message_list, "message": "刪除留言成功"}
        except Exception as e:
            return {"code": "0", "data": None, "message": "刪除留言失敗：" + str(e)}


class ReplyBoard(Resource):
    @jwt_required()
    def post(self):
        try:
            new_reply = request.get_json()
            message_id = new_reply.get("message_id")
            message = MessageModel.get_by_message_id(message_id)

            if not message_id:
                return {"code": "0", "data": None, "message": "請提供 message_id"}

            if not message:
                return {"code": "0", "data": None, "message": "指定的 message 不存在"}

            reply = ReplyModel(
                reply_id=str(uuid.uuid4()).replace("-", ""),
                message_id=new_reply.get("message_id"),
                content=new_reply.get("content"),
                create_account=get_jwt_identity(),
            )

            reply.add()

            reply_list = [
                reply.to_dict()
                for reply in ReplyModel.get_reply_list_by_message_id(
                    new_reply.get("message_id")
                )
            ]
            return {"code": "1", "data": reply_list, "message": "新增回覆成功"}
        except Exception as e:
            return {"code": "0", "data": None, "message": "新增回覆失敗：" + str(e)}

    @jwt_required()
    def put(self, reply_id):
        try:
            reply = ReplyModel.get_by_reply_id(reply_id)

            if not reply:
                return {"code": "0", "data": None, "message": "回覆不存在"}

            temp_reply = request.get_json()
            if reply.create_account != get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號更新回覆"}

            reply.content = temp_reply.get("content")
            reply.update()

            reply_list = [
                reply.to_dict()
                for reply in ReplyModel.get_reply_list_by_message_id(reply.message_id)
            ]
            return {"code": "1", "data": reply_list, "message": "更新回覆成功"}

        except Exception as e:
            return {"code": "0", "data": None, "message": "更新回覆失敗：" + str(e)}

    @jwt_required()
    def delete(self, reply_id):
        try:
            reply = ReplyModel.get_by_reply_id(reply_id)

            if not reply:
                return {"code": "0", "data": None, "message": "回覆不存在"}

            if reply.create_account != get_jwt_identity():
                return {"code": "0", "data": None, "message": "拒絕不同帳號刪除回覆"}

            reply.delete()

            reply_list = [
                reply.to_dict()
                for reply in ReplyModel.get_reply_list_by_message_id(reply.message_id)
            ]
            return {"code": "1", "data": reply_list, "message": "刪除回覆成功"}

        except Exception as e:
            return {"code": "0", "data": None, "message": "刪除回覆失敗：" + str(e)}
