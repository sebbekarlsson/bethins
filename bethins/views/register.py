from flask import Blueprint, render_template
from bethins.forms import UserForm


bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/register', methods=["GET", "POST"])
def render():
    form = UserForm(csrf_enabled=False)

    if form.validate_on_submit():
        email = form.email.data
        user_name = form.user_name.data
        password = form.password.data

        return 'yes'

    return render_template('form.html', form=form)
