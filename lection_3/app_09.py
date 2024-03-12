import email
from flask import Flask
from lection_3.models_05 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Привет!!!'


@app.cli.command('fill-db')
def fill_db():
    # добавляем пользователей
    count = 5
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@example.com')
        db.session.add(new_user)
    db.session.commit()

    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title{post}', content=f'Post content{post}', author=author)
        db.session.add(new_post)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
