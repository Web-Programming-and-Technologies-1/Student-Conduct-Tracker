from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
import json


from App.models import db , Student, User, Review

from App.controllers import (
  # USER CONTROLLERS
    create_user, 
    get_all_users,
    get_all_users_json,
    #STUDENT CONTROLLER
    createStudent,
    getAllStudents,
    getStudent,
    updateStudent,
    # REVIEW CONTROLLER
    createReview,
    getAllReviews
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# ***** PLEASE MODIFY RETURN STATEMENTS FOR FAILED & SUCCESS WITH STATUS CODES WHEN THE API SPEC IS COMPLETED
# WORKS
@user_views.route('/users', methods=['GET'])
def get_user_page():
  try:
    users = get_all_users()
    return render_template('users.html', users=users),200
  except:
    return'ERROR: API Failed to display users.html',404

# WORKS
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

# WORKS
@user_views.route('/static/users')
def static_user_page():
  try:
    return send_from_directory('static', 'static-user.html'),200
  except:
    return'ERROR: API Failed to render static-user.html',404


# get all students
# FIXED
@user_views.route('/', methods=['GET'])
def getallstudents():
  result = []
  students = getAllStudents()
  print(students)
  try:
    for student in students:
       result.append(student.toDict())
    return json.dumps(result),200
  except:
    return'ERROR: API Failed to get all students', 404
  

#search students
#FIXED
@user_views.route('/searchstudent/<id>', methods=['GET'])
def searchStudent(id): #id is the studentID
  try:
    student = getStudent(id)
    return json.dumps(student),202
  except:
    return 'ERROR: API Failed to search for the student', 404

#karma NEED TO FIX
@user_views.route('/karma/<id>', methods=['GET'])
def getKarma(id): #id is the studentID
  try:
    student = getStudent(id)
    studentKarma = student.karma
    return json.dumps(studentKarma),200
  except:
    return'ERROR: API Failed to get student karma score', 404

#add student  
# FIXED
@user_views.route('/add', methods=['POST'])
def addStud():
  try:
      data = request.json
      createStudent(data['studentId'], data['firstname'], data['lastname'], data['username'], data['email'])
      return'PASS: Student created',200
  except:
      return'ERROR: API Failed to create new student', 404

#update student NEED TO FIX
@user_views.route('/update/<id>', methods=['PUT'])
def updateStud(id):
  try: 
    data = request.json
    updateStudent(id, data['studentId'], data['firstname'], data['lastname'], data['username'], data['email'])
    return'PASS: Student updated',200
  except:
    return'ERROR: API Failed to update student', 404

#add a review NEED TO FIX
@user_views.route('/addreview', methods=['POST'])
def createRev():
  try:
      data = request.json
      review = createReview(data["reviewDetails"], data["studentId"], data["id"])
      result = getAllReviews()
      return json.dump(result),200
  except:
    return'ERROR: API Failed to create new review', 404