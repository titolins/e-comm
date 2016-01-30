from flask import (
    render_template,
    url_for,
    request,
    redirect,
    flash,
    jsonify,
    make_response)

from project import app #, session

# import forms and models

# from flask import session as login_session

import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return "To be login page"
