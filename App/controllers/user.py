from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations


def create_user(userId, firstname, lastname, username, email, password):
    newUser = User(userId=userId, firstname=firstname, lastname=lastname,
                   username=username, email=email, password=password)
    try:
        if newUser:
            db.session.add(newUser)
            db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create new staff', 401
    return 'SUCCESS: User created!', 201

# Read operations


def get_user(id):
    return User.query.filter_by(userId=id).first()


def get_all_users():
    return User.query.all()


def get_all_users_toDict():
    users = get_all_users()
    try:
        if users:
            return [user.toDict() for user in users]
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
        return 'ERROR: Failed to update the staff ',401
    return 'SUCCESS: Updated user successfully', 201

# Delete operations


def deleteUser(userId):
    user = get_user(userId)
    try:
        if user:
            user = get_user(userId)
            db.session.delete(user)
            db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to delete the student', 401
    return 'SUCCESS: Deleted user!', 201
