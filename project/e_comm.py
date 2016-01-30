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
from project.models import admin, users, user

from flask import session as login_session

import requests

@app.route('/')
def index():
    return render_template('index.html')

#########################################################
###################### decorators #######################
#########################################################

def login_required(f):
    ''' Decorator for use with pages that require login access
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("You need to login for that!")
            return redirect(url_for('login'))
    return wrap


def user_required(f):
    ''' Decorator for use with pages that require the currently logged in user
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if kwargs['user_id'] == login_session['user_id']:
            return f(*args, **kwargs)
        flash("Only the user may have access to it's profile or delete it")
        return redirect(url_for('index'))
    return wrap


def admin_required(f):
    ''' Decorator for use with pages that require the currently logged in user
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if kwargs['user_access_level'] == login_session['user_access_level']:
            return f(*args, **kwargs)
        flash("Only the user may have access to it's profile or delete it")
        return redirect(url_for('index'))
    return wrap


#########################################################
################### end decorators ######################
#########################################################

#########################################################
######################## CRUD ###########################
#########################################################

##################
# User           #
##################

@app.route('/register')
def showUser():
    return "<p>To be user registration</p>"


@app.route('/user/<int:user_id>/edit')
def editUser(user_id):
    return "<p>To be user {} edit page</p>".format(user_id)


@app.route('/user/<int:user_id>/delete')
def deleteUser(user_id):
    return "<p>To be user {} delete page</p>".format(user_id)


##################
# end User       #
##################

#########################################################
####################### end CRUD ########################
#########################################################

#########################################################
####################### login ###########################
#########################################################

@app.route('/login')
def login():
    return """
        <h1>Login Page</h1>

        <div style='background: lightblue; width: 200px; height:50px;'>
            <a href="{0}">
                Regular user
            </a>
        </div>
        <div style='background: lightgreen; width: 200px; height:50px;'>
            <a href="{1}">
                Admin user
            </a>
        </div>
    """.format(url_for('logRegularUser'), url_for('logAdminUser'))


@app.route('/logout')
def logout():
    del login_session['user_id']
    del login_session['user_access_level']
    del login_session['username']
    del login_session['email']
    return redirect(url_for('index'))

#########################################################
####################### end login #######################
#########################################################

#########################################################
################# development code ######################
#########################################################

@app.route('/login/logRegularUser')
def logRegularUser():
    login_session['user_id'] = user.id_
    login_session['user_access_level'] = user.access_level
    login_session['username'] = user.name
    login_session['email'] = user.name
    return redirect(url_for('index'))

@app.route('/login/logAdminUser')
def logAdminUser():
    login_session['user_id'] = admin.id_
    login_session['user_access_level'] = admin.access_level
    login_session['username'] = admin.name
    login_session['email'] = admin.name
    return redirect(url_for('index'))

#########################################################
################# end development code ##################
#########################################################
