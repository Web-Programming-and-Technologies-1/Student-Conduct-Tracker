from App.models import User, Student, Review
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations
def createReview(reviewId, reviewDetails, studentId, userId):
    review = Review(reviewId=reviewId,reviewDetails = reviewDetails, studentId = studentId, userId = userId)
    try:
        if review:
            db.session.add(review)
            db.session.commit()
            return 'Successfully created review'
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create review'

# Read operations
def getAllReviews():
  return Review.query.all()
 
def getReview(reviewId):
    return Review.query.filter_by(reviewId=reviewId).first()

def getAllReviewsByStudent(studentId):
    return Review.query.filter_by(studentId=studentId).all()

def getAllReviewsByStaff(userId):
    return Review.query.filter_by(userId=userId).all()

def getAllReviews_toDict():
    reviews = getAllReviews()
    if reviews:
        return [review.toDict() for review in reviews]
    return None
        
   
def getAllReviewsByStudent_toDict(studentId):
    reviews = getAllReviewsByStudent(studentId)
    if reviews:
        return [review.toDict() for review in reviews]
    return None

def getAllReviewsByStaff_toDict(userId):
    reviews = getAllReviewsByStaff(userId)
    if reviews:
        return [review.toDict() for review in reviews]
    return None  
   

# Update operations
def updateReview(reviewId, studentId, userId, reviewDetails):
    newReview = getReview(reviewId)
    try:
        if newReview:
           
            newReview.studentId = studentId
            newReview.reviewDetails = reviewDetails
            newReview.userId = userId
            db.session.add(newReview)
            return db.session.commit()
    except:
        db.session.rollback()
        return None

# Delete operations
def deleteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            db.session.delete(review)
            return db.session.commit()
    except:
        db.session.rollback()
        return'ERROR: Failed to delete the review'

# Review upvote logic
def upvoteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            review.upvoteScore = review.upvoteScore + 1
            db.session.add(review)
            return db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to increase the review votes'

# Review downvote logic
def downvoteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            review.downvoteScore = review.downvoteScore + 1
            db.session.add(review)
            return db.session.commit()
    except:
        db.session.rollback()
        return 'ERROR: Failed to decrease the review votes'

