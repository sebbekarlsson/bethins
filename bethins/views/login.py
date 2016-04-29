from flask import Blueprint, render_template
from bethins.forms import LoginForm
from bethins.mongo import db
from bethins.models import User


bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/login', methods=["GET", "POST"])
def render():
    msg = None
    form = LoginForm(csrf_enabled=False)

    if form.validate_on_submit():
        return 'Not implemented yet'
        
    return render_template('login.html', form=form, msg=msg)
