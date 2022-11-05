from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

'''Create operations'''

#Create a new student using the specified information
def create_user(userId, firstname, lastname, username, email, password):
    newUser = User(userId=userId, firstname=firstname, lastname=lastname,
                   username=username, email=email, password=password)
    try:
        db.session.add(newUser)
        db.session.commit()
        return newUser
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create new staff'

# Read operations

'''Read operations'''

# Return user with the specified Id 
def get_user(id):
    return User.query.filter_by(userId=id).first()

# Return all users
def get_all_users():
    return User.query.all()

# Gets and returns all users in dictionary format or None otherwise
def get_all_users_toDict():
    users = get_all_users()
    if users:
        return [user.toDict() for user in users]
    return None


'''Update operations'''
# Get a user based on user ID
# Return none if user not found
# Updates the user details 
# Returns the updated user
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
            db.session.commit()
            return user
    except:
        db.session.rollback()
        return 'ERROR: Failed to update the staff '

# Delete operations

'''Delete Operations'''

# Get a user based n user ID
# Return false if user not found
# Deletes the user if found and return true
def deleteUser(userId):
    user = get_user(userId)
    try:
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
    except:
        db.session.rollback()
        return 'ERROR: Failed to delete the student'
