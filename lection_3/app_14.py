from flask import Flask
from flask_wtf.csrf import CSRFProtect

import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Привет!!!'

@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
    