# import flask_login
from flask_jwt import JWT
from App.models import User

#Authenicate a Staff based on the email and password provided
def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password=password):
        return user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    user = User.query.get(payload['identity'])
    if user:
        return user
    return None

#Remember a user login details 
def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)
    

#Allow user to logout of the system once logged in
def logout_user():
   return flask_login.logout_user()
    

def setup_jwt(app):
    return JWT(app, authenticate, identity)