from .db import db
from datetime import datetime


class CaseStudy(db.Model):
    __tablename__ = "case_studies"

    # Unique identifier for the case study record
    id = db.Column(db.Integer, primary_key=True)

    # Title of the case study
    title = db.Column(db.String(255), nullable=False)

    # A short summary or abstract of the case study
    summary = db.Column(db.String(500))

    # Detailed content describing the case study
    content = db.Column(db.Text, nullable=False)

    # Category for the case study (e.g., "Behavioral Health Housing")
    category = db.Column(db.String(100))

    # Timestamp of when the case study was published
    published_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Optional: Link this case study to a specific service (if applicable)
    # service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    # service = db.relationship('Service', backref='case_studies')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "category": self.category,
            "published_date": self.published_date.isoformat(),
        }
