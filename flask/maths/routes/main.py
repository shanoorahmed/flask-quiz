from flask import Blueprint, render_template
from flask_login import login_required
from maths.models import User
from flask_login.utils import login_required
from sqlalchemy import asc, desc

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/instructions')
def instructions():
    return render_template('instructions.html')

@main.route('/leaderboard')
@login_required
def leaderboard():
    user = User.query.order_by(User.score.desc(), User.last_answered.asc()).limit(10).all()
    size = len(user)
    return render_template('leaderboard.html', user = user, size = size)

@main.route('/thankyou')
@login_required
def thankyou():
    return render_template('thankyou.html')
