import os

from flask import Flask

from anm.db import db, migrate
from anm.messages.views import send_message


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///project.db')
    db.init_app(app)
    migrate.init_app(app, db)

    app.config['AVATAR_URL'] = os.getenv('AVATAR_URL', 'https://picsum.photos/200')
    app.add_url_rule('/', view_func=send_message, methods=['GET', 'POST'])

    return app