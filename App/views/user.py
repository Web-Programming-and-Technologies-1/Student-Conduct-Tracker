from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.models import db , Student, User, Review

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    createStudent
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# ***** PLEASE MODIFY RETURN STATEMENTS FOR FAILED & SUCCESS WITH STATUS CODES WHEN THE API SPEC IS COMPLETED
@user_views.route('/users', methods=['GET'])
def get_user_page():
  try:
    users = get_all_users()
    return render_template('users.html', users=users),200
  except:
    return'ERROR: API Failed to display users.html',404

@user_views.route('/api/users')
def client_app():
  try:
    users = get_all_users_json()
    return jsonify(users), 200
  except:
    return'ERROR: API Failed to get all user',404

# @user_views.route('/api/lol')
# def lol():
#     return 'lol'

@user_views.route('/static/users')
def static_user_page():
  try:
    return send_from_directory('static', 'static-user.html'),200
  except:
    return'ERROR: API Failed to render static-user.html',404


#get all students
@user_views.route('/', methods=['GET'])
def getallstudents():
  result = []
  try:
    students = getAllStudents()
    for student in students:
      result.append(student.toDict())
    return json.dumps(result),200
  except:
    return'ERROR: API Failed to get all students', 404
  

#search students
@user_views.route('/searchstudent/<id>', methods=['GET'])
def searchStudent(id): #id is the studentID
  try:
    student = getStudent(id)
    studentFound = student.toDict()
    return json.dumps(studentFound),202
  except:
    return 'ERROR: API Failed to search for the student', 404

#karma
@user_views.route('/karma/<id>', methods=['GET'])
def getKarma(id): #id is the studentID
  try:
    student = getStudent(id)
    studentKarma = student.karma
    return json.dumps(studentKarma),200
  except:
    return'ERROR: API Failed to get student karma score', 404

#add student  NEED TO FIX
@user_views.route('/add', methods=['POST'])
def addStud():
  try:
      #student = createStudent(firstname, lastname, username, email)
      #result = getAllStudents()
      #return json.dump(result)
      data = request.json
      createStudent(data['firstname'], data['lastname'], data['username'], data['email'])
      return'PASS: Student created',200
  except:
      return'ERROR: API Failed to create new student', 404
    


#update student NEED TO FIX
@user_views.route('/update', methods=['POST'])
def updateStud():
  try:
    data = request.json
    updateStudent(data['studentId'], data['firstname'], data['lastname'], data['username'], data['email'])
    return'PASS: Student updated',200
  except:
    return'ERROR: API Failed to update student', 404

#add a review NEED TO FIX
@user_views.route('/addreview', methods=['POST'])
def createRev(reviewDetails, studentId, userId):
  try:
    review = createReview(reviewDetails, studentId, userId)
    result = getAllReviews()
    return json.dump(result),200
  except:
    return'ERROR: API Failed to create new review', 404