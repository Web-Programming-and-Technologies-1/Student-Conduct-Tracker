 
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
def empty_db(autouse=True, scope="module"):
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
        deleteUser(3)
        assert get_user(3) == None
        
'''Student Controllers Integration Tests -'''

'''Review Controllers Integration Tests -'''

