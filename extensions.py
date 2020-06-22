from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.id

    def __repr__(self):
        return f'<ID {self.id}>'
