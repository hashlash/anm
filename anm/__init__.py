import os

from flask import Flask

from anm.messages.views import send_message


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.add_url_rule('/', view_func=send_message)
    return app