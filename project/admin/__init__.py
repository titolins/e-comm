from flask import Blueprint
from flask import render_template, redirect, request, abort
from flask import session as login_session

bp = Blueprint(
        'admin',
        __name__,
        template_folder='templates',
        static_folder='static',
        )

@bp.before_request
def admin_required():
    ''' Function to restrict access to admin area.
    '''
    if not login_session['user_access_level'] == 1:
        return abort(403)

@bp.route('/panel')
def showPanel():
    return render_template('admin/index.html')

@bp.route('/<int:user_id>/profile')
def profile(user_id):
    return "<h1>To be admin profile page</h1>"

