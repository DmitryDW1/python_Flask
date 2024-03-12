from flask import Flask
from lection_3.models_05 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Привет!!!'


@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    print('Initialized the database.')
    
@app.cli.command('add-user')
def add_user():
    user = User(username=input(), email=input())
    db.session.add(user)
    db.session.commit()
    print(f'User {user.username} added to the database.')
    
@app.cli.command('edit-john')
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print(f'User {user.username} edited in the database.')

if __name__ == '__main__':
    app.run(debug=True)