from flask import render_template


def send_message():
    return render_template('messages/send.html')
