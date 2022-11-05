import os
import tempfile
import pytest
import logging
import unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import *
from App.controllers import *

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''


'''User Model Unit Tests -'''


class UserUnitTests(unittest.TestCase):

    # Test to ensure that user/staff details are being added
    def test_new_user(self):
        user = User(userId=1, firstname="userbob", lastname="bob",
                    username="baloo", email="bob@gmail.com", password="bobpass")
        assert user.username == "baloo"
        assert user.email == "bob@gmail.com"

    # Test to ensure that user/staff details are formatted in a dictionary/JSON format
    def test_user_toDict(self):
        user = User(userId=1, firstname="userbob", lastname="bob",
                    username="baloo", email="bob@gmail.com", password="bobpass")
        userDict = user.toDict()
        self.assertDictEqual(userDict, {"id": 1, "firstname": "userbob",
                             "lastname": "bob", "username": "baloo", "email": "bob@gmail.com"})

    # Test to ensure that user/staff password has is being generated
    def test_set_password(self):
        password = "bobpass"
        hashed = generate_password_hash(password, method='sha256')
        user = User(1, "userbob", "bob", "baloo", "bob@gmail.com", password)
        assert user.password != password

    # Test to ensure that user/staff password is hashed/encrypted
    def test_check_password(self):
        password = "bobpass"
        user = User(1, "userbob", "bob", "baloo", "bob@gmail.com", password)
        assert user.check_password(password) != password


'''Student Model Unit Tests -'''


class StudentUnitTests(unittest.TestCase):

     # Test to ensure that student details are formatted in a dictionary/JSON format
    def test_student_toDict(self):
        student = Student(studentId=1, firstname="bob", lastname="baloo",
                          username="userbob", email="bob@gmail.com")
        studentDict = student.toDict()
        self.assertDictEqual(studentDict, {"id": 1, "firstname": "bob", "lastname": "baloo",
                             "username": "userbob", "email": "bob@gmail.com", "karmaScore": 0.0})


'''Review Model Unit Tests -'''


class ReviewUnitTests(unittest.TestCase):

    # Test to ensure that review details are formatted in a dictionary/JSON format
    def test_review_toDict(self):
        review = Review(reviewId=1, studentId=1, userId=2,
                        reviewDetails="enter review details here")
        reviewDict = review.toDict()
        self.assertDictEqual(reviewDict, {
                             "id": 1, "reviewDetails": "enter review details here", "studentId": 1, "userId": 2, "upvote": 0, "downvote": 0})


'''
   Integration Tests
'''
# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test and deletes it after the test
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update(
        {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


'''Authenication integration test'''

# Ensures authenticate() returns the successfully authenticated user/staff when given the correct credentials. 
# Staff must exist in the database
@pytest.mark.run(order=1) #Controls the execution/call stack order for the test
def test_authenticate():
    user = create_user(userId=1, firstname="userbob", lastname="bob",
                username="baloo", email="bob@gmail.com", password="bobpass")
    assert authenticate("bob@gmail.com", "bobpass") != None


'''User Controllers Integration Tests -'''


class UsersIntegrationTests(unittest.TestCase):

    # Ensure the staff record in the database has the correct values 
    # Ensure the create_user() returns the newly created user
    @pytest.mark.run(order=2)
    def test_create_user(self):
        user = create_user(userId=2, firstname="userbobby", lastname="bobby",
                           username="babloo", email="bobby@gmail.com", password="bobbypass")
        assert user.username == "babloo"

    # Ensure all staff data is being returned in a dictionary/JSON format from the database
    @pytest.mark.run(order=3)
    def test_get_all_users_toDict(self):
        users_dict = get_all_users_toDict()
        self.assertListEqual([{"id": 1, "firstname": "userbob", "lastname": "bob", "username": "baloo", "email": "bob@gmail.com"}, {
                             "id": 2, "firstname": "userbobby", "lastname": "bobby", "username": "babloo", "email": "bobby@gmail.com"}], users_dict)

    # Ensure the staff record in the database has the correct updated values.
    # Ensure the updateUser() returns the updated user
    @pytest.mark.run(order=4)
    def test_updateUser(self):
        user = updateUser(userId=2, firstname="updateTest", lastname="bobby",
                          username="babloo", email="bobby@gmail.com", password="bobbypass")
        assert user.firstname == "updateTest"

    # Ensure the staff record in the database was deleted.
    # Ensure deleteUser() return true after deleting the user
    @pytest.mark.run(order=5)
    def test_deleteUser(self):
        isDeleted = deleteUser(userId=2)
        assert isDeleted == True


'''Student Controllers Integration Tests -'''


class StudentIntegrationTests(unittest.TestCase):

    # Ensure the student record in the database has the correct values 
    # Ensure the createStudent() returns the newly created student
    @pytest.mark.run(order=6)
    def test_createStudent(self):
        student = createStudent(studentId=1, firstname="john", lastname="doe",
                                username="jonny", email="john@gmail.com")
        assert student.username == "jonny"

    # Ensure all student data is being returned in a dictionary/JSON format from the database
    @pytest.mark.run(order=7)
    def test_getAllStudents_toDict(self):
        student_dict = getAllStudents_toDict()
        self.assertListEqual([{"id": 1, "firstname": "john", "lastname": "doe",
                             "username": "jonny", "email": "john@gmail.com", "karmaScore": 0}], student_dict)

    # Ensure the student record in the database has the correct updated values.
    # Ensure the updateStudent() returns the updated student
    @pytest.mark.run(order=8)
    def test_updateStudent(self):
        student = updateStudent(studentId=1, firstname="bob", lastname="doe",
                                username="jonny", email="john@gmail.com")
        assert student.firstname == "bob"

    # Ensure the student karma score is being increased by 1 in the database.
    @pytest.mark.run(order=9)
    def test_increaseKarmaScore(self):
        student = getStudent(1)
        score = student.karmaScore
        student = increaseKarmaScore(1)
        student = getStudent(1)
        assert student.karmaScore == (score + 1)

    # Ensure the student karma score is being decreased by 1 in the database.
    @pytest.mark.run(order=10)
    def test_decreaseKarmaScore(self):
        student = getStudent(1)
        studentScore = student.karmaScore
        if studentScore == 0:
            student = increaseKarmaScore(1)
            studentScore = student.karmaScore
        student = decreaseKarmaScore(1)
        assert student.karmaScore == (studentScore - 1)

    # Ensure the student record in the database was deleted.
    # Ensure deleteStudent() return true after deleting the student.
    @pytest.mark.run(order=11)
    def test_deleteStudent(self):
        isDeleted = deleteStudent(1)
        assert isDeleted == True


'''Review Controllers Integration Tests -'''


class ReviewIntegrationTests(unittest.TestCase):

    # Ensure the review record in the database has the correct values 
    # Ensure the createReview() returns the newly created review
    @pytest.mark.run(order=12)
    def test_createReview(self):
        # Ensures a user/staff exit in the database
        user = create_user(userId=1, firstname="bob", lastname="ross",
                           username="bobby", email="bob@mail.com", password="bobpass") 
        # Ensure a student exit in the database
        student = createStudent(studentId=1, firstname="john", lastname="doe",
                                username="jonny", email="john@gmail.com")
        # Staff Creates a student review 
        review = createReview(reviewId=1, reviewDetails="this is an integration test",
                              studentId=1, userId=1)
        assert review.reviewDetails == "this is an integration test"

    # Ensures that all the reviews from a specific student can be retrieved from the database
    @pytest.mark.run(order=13)
    def test_getAllReviewsByStudent_toDict(self):       
        review_dict = getAllReviewsByStudent_toDict(1)
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}], review_dict)
    
    # Ensures that all the reviews from a specific user/staff can be retrieved from the database
    @pytest.mark.run(order=14)
    def test_getAllReviewsByStaff_toDict(self):
        review_dict = getAllReviewsByStaff_toDict(1)
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}], review_dict)
    
    # Ensures that all the reviews can be retrieved from the database
    @pytest.mark.run(order=15)
    def test_getAllReviews_toDict(self):
        review_dict = getAllReviews_toDict()
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}], review_dict)

    # Ensure the review record in the database has the correct updated values.
    # Ensure the updateReview() returns the updated review                     
    @pytest.mark.run(order=16)
    def test_updateReview(self):
        newReview = updateReview(reviewId=1, studentId=1, userId=1,
                                 reviewDetails="testing update review")
        assert newReview.reviewDetails == "testing update review"

    # Ensure the review upvote score is increased by one in the database.
    @pytest.mark.run(order=17)
    def test_upvoteReview(self):
        review = getReview(1)
        upvoteScore = review.upvoteScore
        review = upvoteReview(1)
        review = getReview(1)
        assert review.upvoteScore == (upvoteScore + 1)

    # Ensure the review downvote score is increased by one in the database.
    @pytest.mark.run(order=18)
    def test_downvoteReview(self):
        review = getReview(1)
        downvoteScore = review.downvoteScore
        review = downvoteReview(1)
        review = getReview(1)
        assert review.downvoteScore == (downvoteScore + 1)

    # Ensure the review record in the database was deleted.
    # Ensure deleteReview() return true after deleting the Review.
    @pytest.mark.run(order=19)
    def test_deleteReview(self):
        isDeleted = deleteReview(1)
        assert isDeleted == True
