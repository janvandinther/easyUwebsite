from app1 import db
from app1 import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f"User('{self.username}')"

class Studyroom(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    open = db.Column(db.Integer, nullable= False)
    spots = db.Column(db.Integer, nullable= False)
    def __repr__(self):
        return f"Studyroom('{self.id}')"
