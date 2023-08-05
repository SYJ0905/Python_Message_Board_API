from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src import db
from src.model.base import Base


class Message(Base):
    message_id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_account = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    replies = relationship(
        "Reply", back_populates="message", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "content": self.content,
            "create_account": self.create_account,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "replies": [reply.to_dict() for reply in self.replies],
        }

    @staticmethod
    def get_message_list():
        return db.session.query(Message).all()

    @staticmethod
    def get_by_message_id(message_id):
        return (
            db.session.query(Message).filter(Message.message_id == message_id).first()
        )


class Reply(Base):
    reply_id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_account = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    message_id = db.Column(
        db.String(36), ForeignKey("message.message_id", ondelete="CASCADE")
    )
    message = relationship("Message", back_populates="replies")

    def to_dict(self):
        return {
            "reply_id": self.reply_id,
            "content": self.content,
            "create_account": self.create_account,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "message_id": self.message_id,
        }

    @staticmethod
    def get_reply_list_by_message_id(message_id):
        message = Message.get_by_message_id(message_id)
        return message.replies

    @staticmethod
    def get_by_reply_id(reply_id):
        return db.session.query(Reply).filter(Reply.reply_id == reply_id).first()
