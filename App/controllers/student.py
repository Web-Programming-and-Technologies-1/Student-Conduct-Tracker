from App.models import  Student
from App.database import db
from sqlalchemy.exc import IntegrityError

'''Create operations'''

# Create a new student using the specified information
def createStudent(studentId, firstname, lastname, username, email):
    student = Student(studentId=studentId, firstname=firstname,
                      lastname=lastname, username=username, email=email)
    try:
        db.session.add(student)
        db.session.commit()
        return student 
    except IntegrityError:
        db.session.rollback()
    return None

'''Read operations'''

# Return all students from the database
def getAllStudents():
    return Student.query.all()

# Get all students from the database
# Returns the students in Dictionary format if found or None otherwise  
def getAllStudents_toDict():
    students = getAllStudents()
    if students:
        return [student.toDict() for student in students]
    return None

# Return a student with a specific Id
def getStudent(studentId):
    return Student.query.filter_by(studentId=studentId).first()

# Get a student using a specific Id
# Return the student in dictionary format or None otherwise
def getStudent_toDict(studentId):
    student = getStudent(studentId)
    if student:
        return student.toDict
    return None
    

'''Update operations'''

# Get a student based on student ID
# Return none if student not found
# Updates the student details 
# Returns the updated student
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
            db.session.commit()
            return student
    except:
        db.session.rollback()
    return None

'''Delete operations'''

# Get a student based n student ID
# Return false if student not found
# Deletes the student if found and return true
def deleteStudent(studentId):
    student = getStudent(studentId)
    try:
        if student:
            db.session.delete(student)
            db.session.commit()
            return True
    except:
        db.session.rollback()
    return False

'''Increase Karma score logic'''

# Gets a student with Id specified 
# Return None if not found
# If found, increase the student karma score by one
# Return student
def increaseKarmaScore(studentId):
    student = getStudent(studentId)
    try:
        if student:
            student.karmaScore = student.karmaScore + 1
            db.session.add(student)
            db.session.commit()
            return student
    except:
        db.session.rollback()
    return None

'''Decrease karma score logic'''

# Gets a student with Id specified 
# Return None if not found
# If found, decrease the student karma score by one
# Return student
def decreaseKarmaScore(studentId):
    student = getStudent(studentId)
    try:
        if student:
            student = getStudent(studentId)
            student.karmaScore = student.karmaScore - 1
            db.session.add(student)
            db.session.commit()
            return student
    except:
        db.session.rollback()

