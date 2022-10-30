import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from App.controllers import *
from App.models import *


'''
   Unit Tests
'''


'''User Model Unit Tests -'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User(userId=1, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
        assert user.username == "baloo"
        assert user.email == "bob@gmail.com"

    def user_test_toDict(self):
        user = User(userId=1, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
        userDict = user.toDict()
        self.assertDictEqual(userDict, {"id":1, "firstname": "bob", "lastname":"baloo","username":"userbob","email":"bob@gmail.com","password":"bobpass"})
    
    def test_set_password(self):
        password = "bobpass"
        hashed = generate_password_hash(password, method='sha256')
        user = User(1, "userbob", "bob", "baloo", "bob@gmail.com", password)
        assert user.password != password

    def test_check_password(self):
        password = "bobpass"
        user = User(1, "userbob", "bob", "baloo", "bob@gmail.com", password)
        assert user.check_password(password) != password


'''Student Model Unit Tests -'''
class StudentUnitTests(unittest.TestCase):

    def student_test_toDict(self):
        student = Student(studentId=1, firstname="bob", lastname="baloo", username="userbob", email="bob@gmail.com")
        studentDict = student.toDict()
        self.assertDictEqual(studentDict, {"id":1,"firstname": "bob", "lastname":"baloo","username":"userbob", "email":"bob@gmail.com","karmaScore":0.0})
    
'''Review Model Unit Tests -'''
class ReviewUnitTests(unittest.TestCase):

    def review_test_toDict(self):
        review = Review(studentId=1, userId=2, reviewDetails="enter review details here")
        reviewDict = review.toDict()
        self.assertDictEqual(reviewDict, {"id":None,"reviewDetails": "enter review details here", "studentId":1,"userId":2, "upvote":0,"downvote":0})
    


