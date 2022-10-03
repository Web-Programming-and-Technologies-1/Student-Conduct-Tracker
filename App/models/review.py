# from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Review(db.Model):
    reviewtId = db.Column(db.Integer, primary_key=True)
    reviewDetails =  db.Column(db.String(50), nullable=False)
    upvote =  db.Column(db.Integer)
    downvote =  db.Column(db.Integer)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
   
    def __init__(self, reviewDetails, upvote, downvote):
        self.reviewDetails = reviewDetails
        self.upvote = upvote
        self.down = downvote


    def toDict(self):
        return{
            'id': self.reviewtId,
            'reviewDetails': self.reviewDetails,
            'upvote': self.upvote,
            'downvote': self.downvote,
        }

    
