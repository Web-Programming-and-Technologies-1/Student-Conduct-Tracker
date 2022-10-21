import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User


from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

# 
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("userbob", "bob", "baloo", "bob@gmail.com","bobpass")
        assert user.username == "userbob"

    def test_toDict(self):
        user = User("userbob", "bob", "baloo", "bob@gmail.com","bobpass")
        userDict = user.toDict()
        self.assertDictEqual(userDict, {"userId":None, "username":"userbob","firstname": "bob", "lastname":"baloo", "email":"bob@gmail.com","password":"bobpass"})
    
    def test_set_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)