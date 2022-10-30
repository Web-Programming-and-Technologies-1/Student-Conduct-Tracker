from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations


def create_user(userId, firstname, lastname, username, email, password):
    try:
        newuser = User(userId=userId, firstname=firstname, lastname=lastname,
                       username=username, email=email, password=password)
        db.session.add(newuser)
        db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to create new staff'

# Read operations


def get_user(id):
    return User.query.filter_by(userId=id).first()


def get_all_users():
    try:
        return User.query.all()
    except:
        return 'ERROR: Failed to get all staffs'


def get_all_users_toDict():
    users = get_all_users()
    try:
        if not users:
            return []
        users = [user.toDict() for user in users]
        return users
    except:
        return 'ERROR: Failed to get all staffs in dictionary format'


# Update operations
def updateUser(userId, username, firstname, lastname, email, password):
    user = get_user(userId)
    try:
        if user:
            user.username = username
            user.firstname = firstname
            user.lastname = lastname
            user.email = email
            user.password = password
            db.session.add(user)
            return db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to update the staff '

# Delete operations


def deleteUser(userId):
    try:
        user = get_user(userId)
        db.session.delete(user)
        db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to delete the student'
