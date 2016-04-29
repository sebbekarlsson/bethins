from flask import Blueprint, render_template
from bethins.forms import UserForm
from bethins.mongo import db
from bethins.models import User


bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/register', methods=["GET", "POST"])
def render():
    msg = None
    form = UserForm(csrf_enabled=False)

    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user_name = form.user_name.data
        password = form.password.data

        existing_user = db.collections.find_one(
                    {
                        'email': email,
                        'nick_name': user_name
                    }
                )

        if existing_user is not None:
            msg = 'User already exists'
        else:
            user = User(
                    email=email,
                    nick_name=user_name,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    role='user',
                    avatar=None,
                    cash=31, 
                    )
            msg = 'Registered!'

            db.collections.insert_one(user.export())

    return render_template('register.html', form=form, msg=msg)
