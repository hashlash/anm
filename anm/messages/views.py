from flask import render_template, request


def send_message():
    from pprint import pprint
    pprint(request.form)
    return render_template('messages/send.html')
