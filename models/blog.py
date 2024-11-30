from utils.db import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for Author
    name = db.Column(db.String(100), nullable=False)  # Name of the author
    email = db.Column(db.String(100), unique=True, nullable=False)  # Unique email for each author
    blogs = db.relationship('Blog', backref='author', lazy=True)  # Relationship to Blog table

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for Blog
    title = db.Column(db.String(100), nullable=False)  # Blog title
    content = db.Column(db.String(5000), nullable=False)  # Blog content
    date = db.Column(db.String(100), nullable=False)  # Date of blog creation
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)  # Foreign key to Author
