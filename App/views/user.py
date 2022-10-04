from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from models import db , Student

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

#get all students
@user_views.route('/', methods=['GET'])
def getallstudents():
  result = []
  students = getAllStudents()
  for student in students:
    result.append(student.toDict())
  return json.dumps(result)

#search students
@user_views.route('/searchstudent/<id>', methods=['GET'])
def searchStudent(id): #id is the studentID
  student = getStudent(id)
  studentFound = student.toDict()
  return json.dumps(studentFound)

#karma
@user_views.route('/karma/<id>', methods=['GET'])
def getKarma(id): #id is the studentID
  student = getStudent(id)
  studentKarma = student.karma
  return json.dumps(studentKarma)

#add student  NEED TO FIX
@user_views.route('/add', methods=['POST'])
def addStud(firstname, lastname, username, email):
    student = createStudent(firstname, lastname, username, email)
    result = getAllStudents()
    return json.dump(result)

#update student NEED TO FIX
@user_views.route('/update', methods=['POST'])
def updateStud(studentId, firstname, lastname, username, email):
    student = updateStudent(studentId, firstname, lastname, username, email)
    result = getStudent(studentId)
    return json.dump(result)

#add a review NEED TO FIX
@user_views.route('/addreview', methods=['POST'])
def createRev(reviewDetails, studentId, userId):
    review = createReview(reviewDetails, studentId, userId)
    result = getAllReviews()
    return json.dump(result)