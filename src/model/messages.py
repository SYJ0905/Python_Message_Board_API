from src import db

# from sqlalchemy.orm import relationship


class Message(db.Model):
    message_id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    # replies = relationship("Reply", back_populates="message")

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "content": self.content,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class Reply(db.Model):
    reply_id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    message_id = db.Column(db.String(36), db.ForeignKey("message.message_id"))

    def to_dict(self):
        return {
            "reply_id": self.reply_id,
            "content": self.content,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "message_id": self.message_id,
        }

    # message = relationship("Message", back_populates="replies")
