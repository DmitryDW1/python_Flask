from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def index_html():
    content = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('index2.html', **content)


if __name__ == '__main__':
    app.run(debug=True)
