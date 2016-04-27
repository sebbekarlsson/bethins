from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/register', methods=["GET", "POST"])
def render():
    return render_template('form.html')
