from flask import Flask, render_template, request, redirect
from utils.db import db
from models.blog import Blog, Author

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(flask_app)

with flask_app.app_context():
    db.create_all()

@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/about')
def about():
    return render_template('about.html')

@flask_app.route('/blogs')
def blogs():
    blogs_list = Blog.query.all()
    return render_template('blogs.html', blogs=blogs_list)

@flask_app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        author_name = request.form['author_name']
        blog_title = request.form['blog_title']
        blog_content = request.form['blog_content']
        blog_date = request.form['blog_date']

        author = Author.query.filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

        new_blog = Blog(
            title=blog_title,
            content=blog_content,
            date=blog_date,
            author_id=author.id
        )
        db.session.add(new_blog)
        db.session.commit()

        return redirect('/blogs')

    return render_template('add_blog.html')


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=8004, debug=True)
