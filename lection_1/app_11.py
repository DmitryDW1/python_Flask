from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет!!!'


@app.route('/main/')
def main():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)


@app.route('/data/')
def data():
    content = {'title': 'База статей'}
    return render_template('data.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
