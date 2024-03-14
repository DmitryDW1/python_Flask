from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'Муж'
    female = 'Жен'
    
class Faculty(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(80), nullable=False)
    student = db.relationship('Student', backref=db.backref(f'faculty'), lazy=True)
   
    def __repr__(self):
        return f'Faculty({self.faculty_name})'

class Evaluation(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id_'), nullable=False)
    
    def __repr__(self):
        return f'Evaluation({self.title}, {self.value})'
    
class Student(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id_'), nullable=False)
    
    

    def __repr__(self):
        return f'Student({self.name}, {self.last_name})'


