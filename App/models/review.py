# from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True)
    reviewDetails =  db.Column(db.String(50), nullable=False)
    upvoteScore =  db.Column(db.Integer)
    downvoteScore =  db.Column(db.Integer)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
   
    def __init__(self, reviewId, reviewDetails):
        self.reviewId = reviewId
        self.reviewDetails = reviewDetails
        self.upvote = 0
        self.down = 0

    def toDict(self):
        return{
            'id': self.reviewId,
            'reviewDetails': self.reviewDetails,
            'upvote': self.upvote,
            'downvote': self.downvote,
        }

    
