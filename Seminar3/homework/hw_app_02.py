# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.


from flask import Flask, render_template
from Seminar3.homework.hw_model_02 import db, Book, Author
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def students():
    book = db.session.query(Book).all()
    return render_template('books.html', books = book)

@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    print('Initialized the database.')


@app.cli.command('fill-authors')
def fill_db():
    # Добавляем авторов
    count = 10
    for i in range(1, count + 1):
        new_author = Author(
                            name=f'Author_{i}',
                            last_name=f'Author_last_name{i}',
                            )
        db.session.add(new_author)
    db.session.commit()

@app.cli.command('fill-books')
def fill_db():
    # Добавляем книги
    count = 10
    for i in range(1, count + 1):
        new_book = Book(
                        book_name=f'Book_{i}',
                        year_of_publication=randint(1955, 2024),
                        number_of_copies=randint(1, 100), 
                        author_id=Author.query.get(randint(1, i)).id_, 
                        )
        db.session.add(new_book)
    db.session.commit()
if __name__ == '__main__':
    app.run(debug=True)