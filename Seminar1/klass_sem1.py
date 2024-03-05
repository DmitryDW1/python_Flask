# Задание №1. Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# Задание №2_1. Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
@app.route('/about/')
def about():
    return 'about me'

# Задание №2_2. ○ страницу "contact".
@app.route('/contact/')
def contact():
    return 'Me contact'

# Задание №3. Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/summa/<int:num1>/<int:num2>/')
def summa(num1, num2):
    return str(num1 + num2)

# Задание №4. Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
@app.route('/len_str/<text>/')
def len_str(text):
    return str(len(text))

# Задание №5. Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".
html = """
    <h1>Моя первая HTML страница</h1>
    <p> Привет, мир! </p>
    """

@app.route('/index/')
def index():
    return html

# Задание №6. Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах. Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл". Данные о студентах должны быть переданы в шаблон через контекст.
_users = [{'name': 'Ivan',
               'Last_name': 'Ivanov',
               'age': '44',
               'average_mark': '4.8'
               },
              {'name': 'Pasha',
               'Last_name': 'Dzen',
               'age': '44',
               'average_mark': '4.8'
               },]

@app.route('/table/')
def table():
    return render_template('table.html', users =_users)

# Задание №7. Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей. Каждый блок должен содержать заголовок новости, краткое описание и дату публикации. Данные о новостях должны быть переданы в шаблон через контекст.
_news = [{'title': 'MAIN_news',
          'content': 'sdsdfsdgsdgsgsfgsfgsfg',
          'date': '2024-02-04'
          },
         {'title': 'other_news',
          'content':'fgsfg',
          'date': '2024-02-05'
          },]

@app.route('/news/')
def news():
    return render_template('news.html', news =_news)


if __name__ == '__main__':
    app.run(debug=True)