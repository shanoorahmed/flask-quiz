from enum import unique
from sqlalchemy.orm import lazyload
from .extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    username = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    college = db.Column(db.Text)
    year = db.Column(db.String(15))
    first_question = db.Column(db.Integer)
    second_question = db.Column(db.Integer)
    third_question = db.Column(db.Integer)
    fourth_question = db.Column(db.Integer)
    fifth_question = db.Column(db.Integer)
    sixth_question = db.Column(db.Integer)
    seventh_question = db.Column(db.Integer)
    eighth_question = db.Column(db.Integer)
    ninth_question = db.Column(db.Integer)
    tenth_question = db.Column(db.Integer)
    eleventh_question = db.Column(db.Integer)
    twelfth_question = db.Column(db.Integer)
    thirteenth_question = db.Column(db.Integer)
    fourteenth_question = db.Column(db.Integer)
    fifteenth_question = db.Column(db.Integer)
    sixteenth_question = db.Column(db.Integer)
    seventeenth_question = db.Column(db.Integer)
    eighteenth_question = db.Column(db.Integer)
    nineteenth_question = db.Column(db.Integer)
    twentieth_question = db.Column(db.Integer)
    question_no = db.Column(db.Integer, nullable=False, default=1)
    score = db.Column(db.Integer,nullable=False, default=200)
    attempt_no = db.Column(db.Integer,nullable=False, default=1)
    bid_value = db.Column(db.Integer,nullable=False, default=0)
    last_answered = db.Column(db.DateTime)
    
    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_number = db.Column(db.Integer, unique=True)
    question_topic = db.Column(db.Text)
    question_img = db.Column(db.Integer)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)  