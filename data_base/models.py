from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(20), index=True)
    surname = db.Column(db.String(20), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password_hash):
        self.password_hash = generate_password_hash(password_hash)
        
    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)
    
