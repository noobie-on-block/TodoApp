from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table

db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(299), nullable=False)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)


class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(299), nullable=False)
    todos = db.relationship('Todo', backref='list')

