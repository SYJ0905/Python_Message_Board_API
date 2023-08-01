from src import db

# from sqlalchemy.orm import relationship


class Message(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    # replies = relationship("Reply", back_populates="message")


class Reply(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    message_id = db.Column(db.String(36), db.ForeignKey("message.id"))
    # message = relationship("Message", back_populates="replies")
