from App.models import User, Review, Student
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations


def createStudent(studentId, firstname, lastname, username, email):
    student = Student(studentId=studentId, firstname=firstname,
                      lastname=lastname, username=username, email=email)
    try:
        if student:
            db.session.add(student)
            return db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create student'


# Read operations


def getAllStudents():
     
    return Student.query.all()
     


def getStudent(studentId):
    return Student.query.filter_by(studentId=studentId).first()


def getAllStudents_toDict():
    students = getAllStudents()
    try:
        if students:
            return [student.toDict() for student in students]
    except:
        return 'ERROR: Failed to get all students in dictionary format'

# Update operations


def updateStudent(studentId, firstname, lastname, username, email):

    student = getStudent(studentId)
    try:
        if student:
            student.studentId = studentId
            student.firstname = firstname
            student.lastname = lastname
            student.username = username
            student.email = email
            db.session.add(student)
            return db.session.commit()
    except:
        db.session.rollback()
        return None
# Delete operations


def deleteStudent(studentId):
    student = getStudent(studentId)
    try:
        if student:
            db.session.delete(student)
            return db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to delete the student'

# increase Karma score logic


def increaseKarmaScore(studentId):
    student = getStudent(studentId)
    try:
        if student:
            student.karmaScore = student.karmaScore + 1
            db.session.add(student)
            return db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to increase karma score'

# decrease karma score logic


def decreaseKarmaScore(studentId):
    student = getStudent(studentId)
    try:
        if student:
            student = getStudent(studentId)
            student.karmaScore = student.karmaScore - 1
            db.session.add(student)
            db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to decrease karma score'
