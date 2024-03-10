import os
from os import abort, error
from pathlib import Path, PurePath
from flask import Flask, flash, make_response, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)

LOGIN = 'admin'
PASSWD = '1234'
CHECK_MESSAGE = 'Неправильный логин или пароль'
CHECK_AGE = 'Вам нет 18 лет'

@app.route('/')
def index():
    return render_template('index.html')

'''
Задача №1

Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.

'''
@app.route('/task_01_button/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return redirect(url_for('hello', name = 'User'))
    return render_template('task_01_button.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name = name)

'''
Задача №2

Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
'''

@app.route('/task_02_upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name_user = secure_filename(file.filename)
        Path(Path.cwd(), 'uploads').mkdir(exist_ok=True)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name_user))
        return redirect(url_for('res_upload_file', file_name = file_name_user))
    return render_template('task_02_upload.html')

@app.route('/res_upload_file/<file_name>')
def res_upload_file(file_name):
    return render_template('res_upload_file.html', name = file_name)

'''
Задача №3

Создать страницу, на которой будет форма для ввода логина и пароля

При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.

'''

@app.route('/task_03_check_user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        get_login = request.form.get('login')
        get_passwd = request.form.get('password')
        if get_login == LOGIN and get_passwd == PASSWD:
            return redirect(url_for('hello', name = get_login))
        else:
            return redirect(url_for('error_403',text = CHECK_MESSAGE))
    return render_template('task_03_check_user.html')

@app.route('/error_403/<text>')
def error_403(text):
    return render_template('error_403.html', text_message_error = text)

'''
Задача №4

Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.

'''

@app.route('/task_04_len_text', methods = ['GET', 'POST'])
def check_text():
    get_text = str(request.form.get('text')).strip()
    if request.method == 'GET':
        return render_template('task_04_len_text.html')
    return render_template('res_len.html', text = len(get_text.split()))

'''
Задача №5

Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.

'''

@app.route('/task_05_math', methods = ['GET', 'POST'])
def math():
    if request.method == 'POST':
        get_number_1 = int(request.form.get('number_1'))
        get_number_2 = int(request.form.get('number_2'))
        operation = request.form.get('operation')
        if operation == '+':
            result = get_number_1 + get_number_2
        elif operation == '-':
            result = get_number_1 - get_number_2
        elif operation == '*':
            result = get_number_1 * get_number_2
        elif operation == '/':
            result = get_number_1 / get_number_2
            if get_number_2 == 0:
                return 'Делить на 0 нельзя!'
        return render_template('res_math.html', result = str(result))
    return render_template('task_05_math.html')

'''
Задача №6

Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.

'''

@app.route('/task_06_check_age', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        get_name = request.form.get('name_user')
        get_age = int(request.form.get('age'))
        if get_age >= 18:
            return redirect(url_for('hello', name = get_name))
        else:
            return redirect(url_for('error_403', text = CHECK_AGE))
    return render_template('task_06_check_age.html')

'''
Задача №7

Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''

@app.route('/task_07_square', methods = ['GET', 'POST'])
def square():
    if request.method == 'POST':
        get_number = int(request.form.get('number'))
        return redirect(url_for('res_square', number = get_number, answer = get_number * get_number ))
    return render_template('task_07_square.html')

@app.route('/res_square/<number>/<answer>')
def res_square(number, answer):
    return render_template('res_square.html', number = number, answer = answer)

'''
Задача №8

Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
'''

@app.route('/task_08_flash', methods=['GET', 'POST'])
def task_08_flash():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Ошибка, введите имя!', 'danger')
            return redirect(url_for('task_08_flash'))
        name = request.form['name']
        flash('Сообщение отправлено', 'success')
        return redirect(url_for('hello_flash', name = name))
    return render_template('task_08_flash.html')

@app.route('/hello_flash/<name>')
def hello_flash(name):
    return render_template('hello_flash.html', name = name)

'''
Задача №9

Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

'''

@app.route('/task_09_cookie', methods=['GET', 'POST'])
def task_09_cookie():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Ошибка, введите имя!', 'danger')
            return render_template('task_09_cookie.html')
        if not request.form['e-mail']:
            flash('Ошибка, введите e-mail!', 'danger')
            return render_template('task_09_cookie.html')
        user_name = request.form['name']
        session['name'] = user_name
        return redirect(url_for('hello_cookie', name = user_name))
    return render_template('task_09_cookie.html')


@app.route('/hello_cookie/<name>', methods=['GET', 'POST'])
def hello_cookie(name):
    if 'name' in session:
        if request.method == 'POST':
            session.pop('name', None)
            return render_template('task_09_cookie.html')
    return render_template('hello_cookie.html', name = name)



if __name__ == '__main__':
    app.run(debug=True)