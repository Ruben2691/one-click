from .db import db
from datetime import datetime

class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    # Unique identifier for the contact message record
    id = db.Column(db.Integer, primary_key=True)

    # Name of the person submitting the contact form
    name = db.Column(db.String(255), nullable=False)

    # Email address of the sender
    email = db.Column(db.String(255), nullable=False)

    # The content of the message submitted by the user
    message = db.Column(db.Text, nullable=False)

    # Timestamp when the message was submitted
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "created_at": self.created_at.isoformat(),
        }
