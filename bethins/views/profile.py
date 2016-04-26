from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/profile', defaults={'id': None})
@bp.route('/profile/<id>')
def render(id):
    return render_template('profile.html', id=id)
