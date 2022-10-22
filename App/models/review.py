from App.database import db


class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True)
    reviewDetails =  db.Column(db.String(50), nullable=False)
    upvoteScore =  db.Column(db.Integer, nullable=False)
    downvoteScore =  db.Column(db.Integer, nullable=False)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
   
    def __init__(self, studentId, userId, reviewDetails):
        self.reviewDetails = reviewDetails
        self.studentId = studentId
        self.userId = userId
        self.upvoteScore = 0
        self.downvoteScore = 0

    def toDict(self):
        return{
            'id': self.reviewId,
            'reviewDetails': self.reviewDetails,
            'studentId' : self.studentId,
            'userId' : self.userId,
            'upvote': self.upvoteScore,
            'downvote': self.downvoteScore,
        }

    
