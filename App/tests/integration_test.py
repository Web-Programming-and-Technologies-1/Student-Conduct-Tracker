import os, tempfile, pytest, logging, unittest

from App.controllers import *
from App.models import *


'''
   Integration Tests
'''
# fixetures are used to setup state in the app before the test
# This fixture creates an empty database for the test and deletes it after the test
@pytest.fixture
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    init_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')

'''Authenication integration test'''

def test_authenticate():
   user = create_user(userId=1, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
   assert authenticate("bob@gmail.com", "bobpass") != None


'''User Controllers Integration Tests -'''
class UsersIntegrationTests(unittest.TestCase):
  
  def test_create_user(self):
      create_user(userId=20, firstname="userbob", lastname="bob", username="baloo", email="bob@gmail.com", password="bobpass")
      assert get_user(20) == "baloo"
      # assert user.username == "baloo"
      # print (user)

'''Student Controllers Integration Tests -'''

'''Review Controllers Integration Tests -'''



