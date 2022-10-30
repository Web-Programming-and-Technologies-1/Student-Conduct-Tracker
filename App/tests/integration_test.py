
import os
import tempfile
import pytest
import logging
import unittest


from App.controllers import *
from App.models import *


'''
   Integration Tests
'''
# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test and deletes it after the test


@pytest.fixture
def empty_db(autouse=True, scope="session"):
    app = create_app(
        {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///temp-database.db'})
    init_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/temp-database.db')


'''Authenication integration test'''


def test_authenticate():
    create_user(userId=1, firstname="userbob", lastname="bob",
                username="baloo", email="bob@gmail.com", password="bobpass")
    assert authenticate("bob@gmail.com", "bobpass") != None


'''User Controllers Integration Tests -'''


class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        create_user(userId=2, firstname="userbobby", lastname="bobby",
                    username="babloo", email="bobby@gmail.com", password="bobbypass")
        user = get_user(2)
        assert user.username == "babloo"

    def test_get_all_users_toDict(self):
        users_dict = get_all_users_toDict()
        self.assertListEqual([{"id": 1, "firstname": "userbob", "lastname": "bob", "username": "baloo", "email": "bob@gmail.com"}, {
                             "id": 2, "firstname": "userbobby", "lastname": "bobby", "username": "babloo", "email": "bobby@gmail.com"}], users_dict)

    def test_updateUser(self):
        create_user(userId=3, firstname="john", lastname="doe",
                    username="jonny", email="john@gmail.com", password="johnpass")
        updateUser(userId=3, firstname="updateTest", lastname="doe",
                   username="jonny", email="john@gmail.com", password="johnpass")
        user = get_user(3)
        assert user.firstname == "updateTest"

    def test_deleteUser(self):
        deleteUser(userId=3)
        assert get_user(3) == None


'''Student Controllers Integration Tests -'''


class StudentIntegrationTests(unittest.TestCase):
    def test_createStudent(self):
        createStudent(studentId=1, firstname="john", lastname="doe",
                      username="jonny", email="john@gmail.com")
        student = getStudent(1)
        assert student.username == "jonny"

    def test_getAllStudents_toDict(self):

        student_dict = getAllStudents_toDict()
        self.assertListEqual([{"id": 1, "firstname": "john", "lastname": "doe",
                             "username": "jonny", "email": "john@gmail.com", "karmaScore": 0}], student_dict)

    def test_updateStudent(self):
        createStudent(studentId=2, firstname="Harry", lastname="potter",
                      username="harrypot", email="harry@gmail.com")
        updateStudent(studentId=2, firstname="bob", lastname="potter",
                      username="harrypot", email="harry@gmail.com")
        student = getStudent(2)
        assert student.firstname == "bob"

    def test_increaseKarmaScore(self):
        createStudent(studentId=3, firstname="Henry", lastname="potter",
                      username="henrypot", email="henry@gmail.com")

        student = getStudent(3)
        score = student.karmaScore
        increaseKarmaScore(3)
        student = getStudent(3)
        newScore = student.karmaScore
        assert newScore == (score + 1)
        deleteStudent(3)

    def test_decreaseKarmaScore(self):
        createStudent(studentId=4, firstname="Henry", lastname="potter",
                      username="henrypot", email="henry@gmail.com")
        student = getStudent(4)
        score = student.karmaScore
        decreaseKarmaScore(4)
        student = getStudent(4)
        newScore = student.karmaScore
        assert newScore == (score - 1)
        deleteStudent(4)

    def test_deleteStudent(self):
        deleteStudent(2)
        assert getStudent(2) == None


'''Review Controllers Integration Tests -'''


class ReviewIntegrationTests(unittest.TestCase):

    def test_createReview(self):
        createReview(reviewId=1, reviewDetails="this is an integration test",
                     studentId=1, userId=1)
        review = getReview(reviewId=1)
        assert review.reviewDetails == "this is an integration test"
        deleteReview(1)

    def test_getAllReviewsByStudent_toDict(self):
        createReview(reviewId=1, reviewDetails="this is an integration test",
                     studentId=1, userId=1)
        createReview(reviewId=2, reviewDetails="this is a 2nd integration test",
                     studentId=1, userId=1)
        review_dict = getAllReviewsByStudent_toDict(1)
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}, {"id": 2, "reviewDetails": "this is a 2nd integration test",
                                                                                        "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}], review_dict)
        deleteReview(1)
        deleteReview(2)

    def test_getAllReviewsByStaff_toDict(self):
        createReview(reviewId=1, reviewDetails="this is an integration test",
                     studentId=1, userId=1)
        createReview(reviewId=2, reviewDetails="this is a 2nd integration test",
                     studentId=1, userId=1)
        review_dict = getAllReviewsByStaff_toDict(1)
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}, {"id": 2, "reviewDetails": "this is a 2nd integration test",
                                                                                        "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}], review_dict)
        deleteReview(1)
        deleteReview(2)

    def test_getAllReviews_toDict(self):
        createReview(reviewId=1, reviewDetails="this is an integration test",
                     studentId=1, userId=1)
        createReview(reviewId=2, reviewDetails="this is a 2nd integration test",
                     studentId=1, userId=2)
        review_dict = getAllReviews_toDict()
        self.assertListEqual([{"id": 1, "reviewDetails": "this is an integration test",
                             "studentId": 1, "userId": 1, "upvote": 0, "downvote": 0}, {"id": 2, "reviewDetails": "this is a 2nd integration test",
                                                                                        "studentId": 1, "userId": 2, "upvote": 0, "downvote": 0}], review_dict)
        deleteReview(1)
        deleteReview(2)

    def test_updateReview(self):
        createReview(reviewId=1, reviewDetails="this is an integration test",
                     studentId=1, userId=1)
        updateReview(reviewId=1, studentId=1, userId=1,
                     reviewDetails="testing update review")
        review = getReview(reviewId=1)
        assert review.reviewDetails == "testing update review"
        deleteReview(1)

    def test_upvoteReview(self):
        createReview(reviewId=1, reviewDetails="testing upvote",
                     studentId=1, userId=1)
        review = getReview(1)
        upvoteScore = review.upvoteScore
        upvoteReview(1)
        review = getReview(1)
        newUpvoteScore = review.upvoteScore
        assert newUpvoteScore == (upvoteScore + 1)
        deleteReview(1)

    def test_downvoteReview(self):
        createReview(reviewId=1, reviewDetails="testing downvote",
                     studentId=1, userId=1)
        review = getReview(1)
        downvoteScore = review.downvoteScore
        downvoteReview(1)
        review = getReview(1)
        newdownvoteScore = review.downvoteScore
        assert newdownvoteScore == (downvoteScore + 1)
        deleteReview(1)
