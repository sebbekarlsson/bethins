from flask import Flask
from bethins.views.index import bp as index_bp
from bethins.views.profile import bp as profile_bp

from bethins.api.site import is_loggedin

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(profile_bp)

app.jinja_env.globals.update(is_loggedin=is_loggedin)
