from flask import session


def is_loggedin():
    if "user_id" in session:
        if len(session["user_id"]) >= 1:
            if session['user_id'] != '':
                return True

    return False
