import os, tempfile, pytest, logging, unittest
# from test_flaskr import *
from werkzeug.security import check_password_hash, generate_password_hash

from App.models import User


from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

# 
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User(userId=1, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
        assert user.username == "userbob"
        assert user.email == "bob@mail.com"

    def user_test_toDict(self):
        user = User(userId=1, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
        userDict = user.toDict()
        self.assertDictEqual(userDict, {"id":1, "firstname": "bob", "lastname":"baloo","username":"userbob","email":"bob@gmail.com","password":"bobpass"})
    
    def test_set_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password) != password