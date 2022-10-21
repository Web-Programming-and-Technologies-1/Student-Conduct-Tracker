import os, tempfile, pytest, logging, unittest
# from test_flaskr import *
from App.models import Review


from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit tests

'''

class ReviewUnitTests(unittest.TestCase):

    def test_toDict(self):
        review = Review(studentId=1, userId=2, reviewDetails="enter review details here")
        reviewDict = review.toDict()
        self.assertDictEqual(reviewDict, {"id":None,"reviewDetails": "enter review details here", "studentId":1,"userId":2, "upvote":0,"downvote":0})
    
   