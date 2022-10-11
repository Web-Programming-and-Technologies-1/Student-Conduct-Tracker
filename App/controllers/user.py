from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

# Added error handling to the functions below provided within the MVC template
def get_all_users():
    try:
        return User.query.all()
    except:
        return 'ERROR: Failed to get all users'


def create_user(userId, firstname, lastname, username, email, password):
    try:
        newuser = User(userId=userId, firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        db.session.add(newuser)
        db.session.commit()
    except:
        return 'ERROR: Failed to create new user'

def get_all_users_json():
    try:
        users = User.query.all()
        if not users:
            return []
        users = [user.toDict() for user in users]
        return users
    except:
        return 'ERROR: Failed to get all users in JSON Format'

def get_all_users():
    try:
        return User.query.all()
    except:
        return'ERROR: Failed to all users'