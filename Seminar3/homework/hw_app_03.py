# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

# Для заполнения таблиц используйте команды:
# 1) initdb
# 2) fill-db
# 3) fill-evaluations


from flask import Flask, render_template
from hw_models_03 import Evaluation
from hw_models_03 import Gender, db, Student, Faculty
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_2.db'
db.init_app(app)

COUNT = 10

@app.route('/')
def students():
    students = db.session.query(Student).all()
    student_evaluations = db.session.query(Evaluation).all()
    return render_template('students.html', student=students, evaluations=student_evaluations)

@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('fill-db')
def fill_db():
    """
    Заполнение таблиц студентов и факультетов в базе данных.
    """
    # Добавляем студентов
    for student in range(1, COUNT + 1):
        new_student = Student(
                                name=f'student{student}', 
                                last_name=f'last_name{student}',
                                age=choice([student, student * 5]), 
                                gender=choice([Gender.male, Gender.female]), 
                                group=f'group{student}', faculty_id=randint(1, 10,), 
                                email=f'student{student}@example.com'
                            )
        db.session.add(new_student)
    db.session.commit()

    
    # Добавляем факультеты
    for faculty in range(1, COUNT + 1):
        new_faculty = Faculty(faculty_name=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    

@app.cli.command('fill-evaluations')
def fill_evaluations():
    """
    Заполнение таблицы оценок в базе данных.
    """
    for student in range(1, COUNT + 1):
        for evaluation in range(1, 4):
            new_evaluation = Evaluation(
                title=f'Academic_discipline{evaluation}', 
                value=randint(1, 5),
                student_id=Student.query.get(student).id_, 
            )
            db.session.add(new_evaluation)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)