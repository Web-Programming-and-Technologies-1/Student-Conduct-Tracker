from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

#Create operations
def create_user(userId, firstname, lastname, username, email, password):
    try:
        newuser = User(userId=userId, firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        db.session.add(newuser)
        db.session.commit()
    except:
        return 'ERROR: Failed to create new staff'

#Read operations
def get_user(id):
    try:
        return User.query.get(id)
    except:
        return "ERROR: Failed to get staffs"


def get_all_users():
    try:
        return User.query.all()
    except:
        return 'ERROR: Failed to get all staffs'

#Update operations
def updateUser(userId, username, firstname, lastname, email, password ):
    try:
        user = get_user(userId)
        user.username = username,
        user.firstname = firstname,
        user.lastname = lastname,
        user.email = email,
        user.password = password
        db.session.add(user)
        db.session.commit()
    except:
        return 'ERROR: Failed to update the staff '

#Delete operations
def deleteUser(userId):
    try:
        user = get_user(userId)
        db.session.delete(user)
        db.session.commit()
    except:
        return'ERROR: Failed to delete the student'