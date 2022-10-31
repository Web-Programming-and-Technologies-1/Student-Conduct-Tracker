from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

import json


from App.models import db , Student, User, Review

from App.controllers import * 
"""
(
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
    getAllReviews,
    
)
"""

user_views = Blueprint('user_views', __name__, template_folder='../templates')

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


@user_views.route('/static/users')
def static_user_page():
  try:
    return send_from_directory('static', 'static-user.html'),200
  except:
    return'ERROR: API Failed to render static-user.html',404


##
@user_views.route('/', methods=['GET'])
@jwt_required()
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
@user_views.route('/searchstudent/<id>', methods=['GET'])
@jwt_required()
def searchStudent(id): 
  try:
    student = getStudent(id)
    return json.dumps(student.toDict()),202
  except:
    return 'ERROR: API Failed to search for the student', 404

#karma 
@user_views.route('/karma/<id>', methods=['GET'])
@jwt_required()
def getKarma(id): 
  try:
    student = getStudent(id)
    studentKarma = student.karmaScore
    return json.dumps(studentKarma),200
  except:
    return'ERROR: API Failed to get student karma score', 404

@user_views.route('/upvote/<reviewId>/<studentId>', methods=['POST'])
@jwt_required()
def createUpvote(reviewId,studentId): 
  try:
    upvoteReview(reviewId)
    increaseKarmaScore(studentId)
    return 'PASS: Review Upvoted and Karma Score Increased', 200
  except:
    return'ERROR: API Failed to upvote review and increase student karma score', 404

@user_views.route('/downvote/<reviewId>/<studentId>', methods=['POST'])
@jwt_required()
def createDownvote(reviewId,studentId): 
  try:
    downvoteReview(reviewId)
    decreaseKarmaScore(studentId)
    return 'PASS: Review Downvoted and Karma Score Decreased', 200
  except:
    return'ERROR: API Failed to downvote review and decrease student karma score', 404
  

#add student  
@user_views.route('/add', methods=['POST'])
@jwt_required()
def addStud():
  try:
      data = request.json
      createStudent(data['studentId'], data['firstname'], data['lastname'], data['username'], data['email'])
      return'PASS: Student created',200
  except:
      return'ERROR: API Failed to create new student',404

#update student 
@user_views.route('/update/<id>', methods=['PUT'])
@jwt_required()
def updateStud(id):
  try: 
    student = Student.query.filter_by(studentId=id).first()
    if student == None:
      return 'ERROR: Student ID not found',404
    data = request.get_json()
    
    if 'firstname' in data:
      student.firstname = data['firstname']
    if 'lastname' in data:
      student.lastname = data['lastname']
    if 'username' in data:
      student.username = data['username']
    if 'email' in data:
      student.email = data['email']
    db.session.add(student)
    db.session.commit()
    return 'PASS: Student updated',200
  except:
    return'ERROR: API Failed to update student', 404

#add a review 
@user_views.route('/addreview', methods=['POST'])
@jwt_required()
def createRev():
    try:
      data = request.get_json()
      review=createReview(data['reviewId'],data['reviewDetails'], data['studentId'], data['userId'])
      return 'PASS: Review Created',200
    except:
      return'ERROR: API Failed to create new review', 404
    


@user_views.route('/users', methods=['POST'])
def addUser():
  try:
    data = request.get_json()
    create_user(data['userId'], data['firstname'], data['lastname'], data['username'], data['email'], data['password'])
    return 'PASS: User Created',200
  except:
      return'ERROR: API Failed to create new user', 404  

@user_views.route('/viewusers', methods=['GET'])
def getUser():
  result = []
  user = get_all_users_json()
  return user 

@user_views.route('/getallreviews', methods=['GET'])
@jwt_required()
def getallreviews():
  result = []
  reviews = getAllReviews()
  print(reviews)
  try:
     for review in reviews:
         result.append(review.toDict())
     return json.dumps(result),200
  except:
     return'ERROR: API Failed to get all reviews', 404