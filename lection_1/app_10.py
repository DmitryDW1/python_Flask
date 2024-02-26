from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет!!!'


@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
               'mail': 'nik@rambler.ru',
               'phone': '8-908-908-33-33',
               },
              {'name': 'Феофан',
               'mail': 'feo@rambler.ru',
               'phone': '8-908-908-55-55',
               },
              {'name': 'Оверран',
               'mail': 'ove@rambler.ru',
               'phone': '8-908-555-33-99',
               }, ]

    content = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('users.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
