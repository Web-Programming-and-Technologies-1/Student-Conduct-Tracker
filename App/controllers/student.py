from App.models import  User, Review, Student
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations
def createStudent(firstname, lastname, username, email ):
    student = Student(firstName=firstName, lastName=lastName, username = username, email=email)
    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create student'
    return 'Successfully created student'

# Read operations

def getAllStudents():
    try:
       return Student.query.all()
    except:
        return 'ERROR: Failed to find all the students'

def getStudent(studentId):
    try:
        return Student.query.filter_by(studentId=studentId).first()
    except:
        return 'ERROR: Failed to get the student'

# Update operations
def updateStudent(studentId, firstname, lastname, username, email):
    try:
        student = getStudent(studentId)
        student.firstName = firstName,
        student.lastName = lastName,
        student.username = username,
        student.email = email,
        db.session.add(student)
        db.session.commit()
    except:
        return 'ERROR: Failed to update the student '
# Delete operations

def deleteStudent(studentId, userId):
    try:
        student = getReview(studentId, userId)
        db.session.delete(student)
        db.session.commit()
    except:
        return'ERROR: Failed to delete the student'

# increase Karma score logic
def increaseKarmaScore (studentId):
    try:
        student = Student.query.filter_by(studentId=studentId).first()
        student.karma = student.karma + 1
        db.session.add(student)
        db.session.commit()
    except:
        return 'ERROR: Failed to increase karma score'

# decrease karma score logic
def decreaseKarmaScore(studentId):
    try:
        student = Student.query.filter_by(studentId=studentId).first()
        student.karma = student.karma - 1
        db.session.add(student)
        db.session.commit()
    except:
        return 'ERROR: Failed to decrease karma score'
