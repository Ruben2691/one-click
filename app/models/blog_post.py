from .db import db
from datetime import datetime

class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    # Unique identifier for the blog post
    id = db.Column(db.Integer, primary_key=True)

    # Title of the blog post
    title = db.Column(db.String(255), nullable=False)

    # The body/content of the blog post
    content = db.Column(db.Text, nullable=False)

    # Foreign key to the user who authored the post
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Timestamp when the blog post was created
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Timestamp when the blog post was last updated
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationship to the User model for easy access to author details
    author = db.relationship("User", backref="blog_posts")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author.to_dict() if self.author else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
