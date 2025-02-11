from .db import db


class Service(db.Model):
    __tablename__ = "services"

    # Unique identifier for the service record
    id = db.Column(db.Integer, primary_key=True)

    # The name of the service (e.g., "Funding Readiness")
    name = db.Column(db.String(100), nullable=False)

    # A brief description of what the service entails
    description = db.Column(db.Text, nullable=False)

    # Detailed information about the service (optional extra details)
    details = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "details": self.details,
        }
