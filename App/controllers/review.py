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

def getReview(reviewId, userId):
    try:
        return Review.query.filter_by(reviewId=reviewId, userId=userId).first()
    except:
        return 'ERROR: Failed to get the review'

# Update operations
def updateReview(reviewId, reviewDetails, userId):
    try:
        newReview = getReview(reviewId, userId)
        newReview.reviewDetails = reviewDetails,
        db.session.add(newReview)
        db.session.commit()
    except:
        return 'ERROR: Failed to update the review'

# Delete operations
def deleteReview(reviewId, userId):
    try:
        review = getReview(reviewId, userId)
        db.session.delete(review)
        db.session.commit()
    except:
        return'ERROR: Failed to delete the review'

# Review upvote logic
def upvoteReview(reviewId):
    try:
        review = Review.query.filter_by(reviewId=reviewId).first()
        review.upvoteScore = review.upvoteScore + 1
        # karmaScore = increaseKarmaScore (studentId)
        db.session.add(review)
        db.session.commit()
    except:
        return 'ERROR: Failed to increase the review votes'

# Review downvote logic
def downvote_review(reviewId):
    try:
        review = Review.query.filter_by(reviewId=reviewId).first()
        review.downvoteScore = review.downvoteScore + 1
        db.session.add(review)
        db.session.commit()
    except:
        return 'ERROR: Failed to decrease the review votes'