from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'Муж'
    female = 'Жен'
    

class Author(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    book = db.relationship('Book', backref=db.backref(f'author'), lazy=True)

    def __repr__(self):
        return f'Author({self.name}, {self.last_name})'
class Book(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    year_of_publication = db.Column(db.Integer, nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id_'), nullable=False)
   
    def __repr__(self):
        return f'Book({self.book_name})'