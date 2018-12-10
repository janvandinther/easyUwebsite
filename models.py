from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_username):
    return User.query.get(user_username)




class User(db.Model, UserMixin):
    username = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{self.username}, '{self.email}', '{self.image_file}''"

    def get_id(self):
        return self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)

    def __repr__(self):
        return "User('{self.title}, '{self.date_posted}''"



class StudyRoom(db.Model):
    study_room = db.Column(db.String, primary_key=True)
    opening_hours = db.Column(db.String, nullable=False)

    available_spots = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "Study Room('{self.study_room}, '{self.opening_hours}', '{self.available_spots', '{self.address}' ' "

    def add_study_rooms():
        study_rooms = [['Aula1', 'Mon-Fry: 8.30-19.30', 100, 'Sede Centrale'],
                       ['Aula2', 'Mon-Fry: 8.30-19.30', 100, 'Sede Centrale']]

        for s in range(study_rooms.__len__()):
            st = StudyRoom(study_room=study_rooms[s][0], opening_hours=study_rooms[s][1],
                           available_spots=study_rooms[s][2], address=study_rooms[s][3])
            db.session.add(st)
            db.session.commit()