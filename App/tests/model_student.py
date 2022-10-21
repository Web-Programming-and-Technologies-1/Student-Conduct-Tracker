import os, tempfile, pytest, logging, unittest
# from test_flaskr import *
from App.models import Student


from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit tests

'''

class StudentUnitTests(unittest.TestCase):

    def test_toDict(self):
        student = Student(studentId=1, firstname="bob", lastname="baloo", username="userbob", email="bob@gmail.com")
        studentDict = student.toDict()
        self.assertDictEqual(studentDict, {"id":1,"firstname": "bob", "lastname":"baloo","username":"userbob", "email":"bob@gmail.com","karmaScore":0.0})
    
   