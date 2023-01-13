from flask import render_template, request

from anm.db import db
from anm.messages.models import Message


def send_message():
    if request.method == "POST":
        message = Message(message=request.form['message'])
        db.session.add(message)
        db.session.commit()
        return render_template('messages/send.html', message_sent=True)
    return render_template('messages/send.html')
