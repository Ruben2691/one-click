from datetime import datetime
from .db import db


class Page(db.Model):
    __tablename__ = "pages"

    # Unique identifier for the page
    id = db.Column(db.Integer, primary_key=True)

    # The title of the page (e.g., "About Us", "Home")
    title = db.Column(db.String(255), nullable=False)

    # A URL-friendly string to uniquely identify the page
    slug = db.Column(db.String(255), nullable=False, unique=True)

    # The main content of the page (could be HTML, markdown, etc.)
    content = db.Column(db.Text, nullable=False)

    # Timestamp indicating when the page was last updated
    last_updated = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "content": self.content,
            "last_updated": self.last_updated.isoformat(),
        }
