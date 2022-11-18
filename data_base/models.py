from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = '/unauthorization'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(20), index=True)
    surname = db.Column(db.String(20), index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password_hash):
        return generate_password_hash(password_hash)
        
    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)
    
    def get_id(self):
        return str(self.id)
    
    def to_json(self):
        return {
            "name": self.name,
            "surname": self.surname
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_post = db.Column(db.String(240))
    publication_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='post')

    def __repr__(self):
        return '<Post {}>'.format(self.text_post)
    
    def to_json(self):
        return {
            "text_post": self.text_post,
            "publication_date": str(self.publication_date),
            "author_name": self.user.name,
            "author_surname": self.user.surname
        }
