from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


#--------------------------Admin Required-------------------------------
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_admin():
            # return redirect(url_for('login'))
            return {'message': "Shhh! It's a secret for Admin only!"}
        return f(*args, **kwargs)
    return decorated_function

def is_admin():
    """
    Checks to make sure logged in user is admin
    """
    if current_user.account_type == "Admin":
        return True
    else:
        return False
