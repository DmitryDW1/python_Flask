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
    
@app.cli.command('add-john')
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print(f'User {user.username} added to the database.')
    
    
if __name__ == '__main__':
    app.run(debug=True)