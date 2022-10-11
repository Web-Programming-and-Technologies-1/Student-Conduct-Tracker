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
    return json.dumps(student.toDict()),202
  except:
    return 'ERROR: API Failed to search for the student', 404

#karma FIXED
@user_views.route('/karma/<id>', methods=['GET'])
def getKarma(id): #id is the studentID
  try:
    student = getStudent(id)
    studentKarma = student.karmaScore
    return json.dumps(studentKarma),200
  except:
    return'ERROR: API Failed to get student karma score', 404

@user_views.route('/upvote/<reviewId>/<studentId>', methods=['POST'])
def createUpvote(reviewId,studentId): 
  try:
    upvoteReview(reviewId)
    #upvotereview=upvoteReview(reviewId)
    #print(upvotereview)
    increaseKarmaScore(studentId)
    
    return 'PASS: Review Upvoted and Karma Score Increased', 200
  except:
    return'ERROR: API Failed to upvote review and increase student karma score', 404

@user_views.route('/downvote/<reviewId>/<studentId>', methods=['POST'])
def createDownvote(reviewId,studentId): 
  try:
    downvoteReview(reviewId)
    #print(downvotescore)
    decreaseKarmaScore(studentId)
    
    return 'PASS: Review Downvoted and Karma Score Decreased', 200
  except:
    return'ERROR: API Failed to downvote review and decrease student karma score', 404
  

#add student  
# FIXED
@user_views.route('/add', methods=['POST'])
def addStud():
  try:
      data = request.json
      createStudent(data['studentId'], data['firstname'], data['lastname'], data['username'], data['email'])
      return'PASS: Student created',200
  except:
      return'ERROR: API Failed to create new student',404

#update student NEED TO FIX
@user_views.route('/update/<id>', methods=['PUT'])
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
  
    #updateStudent(studentId=id, firstname=student.firstname, lastname=student.lastname, username=student.username, email=student.email)
    #updateStudent(studentId=['studentId'], firstname=data['firstname'], lastname=data['lastname'], username=data['username'], email=data['email'])
    ##return json.dumps(student.toDict()),202
    return 'PASS: Student updated',200
  except:
    return'ERROR: API Failed to update student', 404

#add a review NEED TO FIX
@user_views.route('/addreview', methods=['POST'])
def createRev():
  
    try:
      data = request.get_json()
      review=createReview(data['reviewDetails'], data['studentId'], data['userId'])
      #result = getAllReviews()
      #return review
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