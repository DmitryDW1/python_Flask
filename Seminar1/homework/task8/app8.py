from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)

@app.route('/main/')
def main():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)



@app.route('/about/')
def about():
    content = {'title': 'О нас'}
    return render_template('about.html', **content)


@app.route('/contacts/')
def contacts():
    content = {'title': 'Контакты'}
    return render_template('contacts.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
