from datetime import datetime
from demo import db

class StudentRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(120))
    password = db.Column(db.String(60))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

