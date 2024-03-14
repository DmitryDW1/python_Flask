from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from form_3 import LoginForm

import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Привет!!!'

@app.route('/login', methods=['GET', 'POST'])
@csrf.exempt
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)