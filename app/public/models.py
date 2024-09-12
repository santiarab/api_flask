from flask_login import UserMixin
from sqlalchemy.testing.suite.test_reflection import users

from app import db
from sqlalchemy.sql import func


def update():
    db.session.commit()


class Task(db.Model, UserMixin):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, nullable=False, default=False)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, title, user_id, description=None, due_date=None):
        self.title = title
        self.user_id = user_id
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f'<Task {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title=None, description=None, due_date=None, status=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat()
        }

    @staticmethod
    def get_by_id(user_id,id):
        return Task.query.filter_by(user_id=user_id, id=id).first()

    @staticmethod
    def get_by_title(title):
        return Task.query.filter_by(title=title).first()

    @staticmethod
    def get_all():
        return Task.query.all()

    @staticmethod
    def get_all_by_user(user_id):
        return Task.query.filter_by(user_id=user_id)