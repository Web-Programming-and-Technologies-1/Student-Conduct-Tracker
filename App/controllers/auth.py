import flask_login
from flask_jwt import JWT
from App.models import User

#Added error handling to the functions below provided within the MVC template
def authenticate(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
    except:
        return'ERROR: Failed to authenticate user'

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    try:
        return User.query.get(payload['identity'])
    except:
        return 'ERROR: Failed to identify user'

def login_user(user, remember):
    try:
        return flask_login.login_user(user, remember=remember)
    except:
        return 'ERROR: Failed to remember user'


def logout_user():
    try:
        flask_login.logout_user()
    except:
        return 'ERROR: Failed to log out users'

def setup_jwt(app):
    return JWT(app, authenticate, identity)