from src import db

# from sqlalchemy.orm import relationship


class Message(db.Model):
    message_id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_account = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    # replies = relationship("Reply", back_populates="message")

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "content": self.content,
            "create_account": self.create_account,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_message_list():
        return db.session.query(Message).all()

    @staticmethod
    def get_by_message_id(message_id):
        return (
            db.session.query(Message).filter(Message.message_id == message_id).first()
        )


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
