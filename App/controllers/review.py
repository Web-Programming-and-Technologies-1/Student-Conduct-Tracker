from App.models import User, Student, Review
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations
def createReview(reviewDetails, studentId, userId):
    review = Review(reviewDetails = reviewDetails, studentId = studentId, userId = userId)
    try:
        db.session.add(review)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create review'
    return 'Successfully created review'

# Read operations
def getAllReviews():
    try:
       return Review.query.all()
    except:
        return 'ERROR: Failed to find all the reviews'

def getReview(reviewtId, userId):
    try:
        return Review.query.filter_by(reviewtId=reviewtId, userId=userId).first()
    except:
        return 'ERROR: Failed to get the review'

# Update operations
def updateReview(reviewtId, reviewDetails, userId):
    try:
        newReview = getReview(reviewtId, userId)
        newReview.reviewDetails = reviewDetails,
        db.session.add(newReview)
        db.session.commit()
    except:
        return 'ERROR: Failed to update the review'

# Delete operations
def deleteReview(reviewtId, userId):
    try:
        review = getReview(reviewtId, userId)
        db.session.delete(review)
        db.session.commit()
    except:
        return'ERROR: Failed to delete the review'

# Review upvote logic
def upvoteReview(reviewtId, studentId):
    try:
        review = Review.query.filter_by(reviewtId=reviewtId).first()
        review.upvoteScore = review.upvoteScore + 1
        # karmaScore = increaseKarmaScore (studentId)
        db.session.add(review)
        db.session.commit()
    except:
        return 'ERROR: Failed to increase the review votes'

# Review downvote logic
def downvote_review(reviewtId):
    try:
        review = Review.query.filter_by(reviewtId=reviewtId).first()
        review.downvoteScore = review.downvoteScore + 1
        db.session.add(review)
        db.session.commit()
    except:
        return 'ERROR: Failed to decrease the review votes'