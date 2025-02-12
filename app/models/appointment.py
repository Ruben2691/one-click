from .db import db
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = "appointments"

    # Unique identifier for the appointment record
    id = db.Column(db.Integer, primary_key=True)

    # Optional: Foreign key referencing the user who scheduled the appointment (could be null for guests)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    # The date and time when the appointment is scheduled
    scheduled_time = db.Column(db.DateTime, nullable=False)

    # Optional notes about the appointment (e.g., topics to discuss)
    notes = db.Column(db.Text)

    # Timestamp when the appointment was created in the system
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to the User model to access the scheduling user’s details
    user = db.relationship("User", backref="appointments")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "scheduled_time": self.scheduled_time.isoformat(),
            "notes": self.notes,
            "created_at": self.created_at.isoformat(),
        }
