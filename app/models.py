from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(299), nullable=False)
    todos = db.relationship('Todo', backref='list',
                            cascade="all, delete-orphan")


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(299), nullable=False, unique=True)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)
