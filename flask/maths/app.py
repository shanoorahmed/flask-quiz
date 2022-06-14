from flask import Flask, render_template
import os, time
from datetime import datetime, timedelta

from .extensions import db, login_manager
from .routes.auth import auth
from .routes.main import main
from .routes.question import question
from .commands import create_db
from maths.models import User

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbmasteruser:{UDL7t<KCK-:dgiu??-NCkyAdm]F#c1(@ls-914ac82b520ae838ad0dad273f48e393bb0fc473.c3s2wzmwyt4k.ap-south-1.rds.amazonaws.com/postgres"
    app.config["SECRET_KEY"] = "5a269165b9f335e9944cb680"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    os.environ['TZ'] = 'Asia/Kolkata'
    time.tzset()

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "User needs to be logged in to view this page!"
    login_manager.login_message_category = "warning"
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(question)

    app.cli.add_command(create_db)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'),404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'),500

    return app