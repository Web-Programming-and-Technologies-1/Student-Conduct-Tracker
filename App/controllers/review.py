from App.models import  Review 
from App.database import db
from sqlalchemy.exc import IntegrityError

from .user import (
    get_user
)
from .student import (
    getStudent
)


'''Create operations'''

# Checks to verify that the staff exist within the system
# Checks to verify that the student information exist within the system
# Creates a review if both staff and student exist and None otherwise
def createReview(reviewId, reviewDetails, studentId, userId):
    user = get_user(userId)
    student = getStudent(studentId)
    try:
        if user and student:
            review = Review(reviewId=reviewId, reviewDetails=reviewDetails,
                            studentId=studentId, userId=userId)
            db.session.add(review)
            db.session.commit()
            return review
    except IntegrityError:
            db.session.rollback()
    return None


'''Read operations'''

# Return all reviews from the database
def getAllReviews():
    return Review.query.all()

# Get all reviews from the database
# Returns the reviews in Dictionary format if found or None otherwise
def getAllReviews_toDict():
    reviews = getAllReviews()
    if reviews:
        return [review.toDict() for review in reviews]
    return None

# Return a review with a specific Id
def getReview(reviewId):
    return Review.query.filter_by(reviewId=reviewId).first()

# Get a review using a specific Id
# Return the review in dictionary format or None otherwise
def getReview_toDict(reviewId):
    review = getReview(reviewId)
    if review:
        return review.toDict
    return None

# Return all reviews from a specific student
def getAllReviewsByStudent(studentId):
    return Review.query.filter_by(studentId=studentId).all()

# Get a review from a specific student
# Return the reviews in dictionary format or None otherwise
def getAllReviewsByStudent_toDict(studentId):
    reviews = getAllReviewsByStudent(studentId)
    if reviews:
        return [review.toDict() for review in reviews]
    return None

# Review all reviews from a specific staff
def getAllReviewsByStaff(userId):
    return Review.query.filter_by(userId=userId).all()

# Get a review from a specific staff
# Return the reviews in dictionary format or None otherwise
def getAllReviewsByStaff_toDict(userId):
    reviews = getAllReviewsByStaff(userId)
    if reviews:
        return [review.toDict() for review in reviews]
    return None


'''Update operations'''

# Get a review based on review ID
# Return none if review not found
# Updates the review details 
# Returns the updated review
def updateReview(reviewId, studentId, userId, reviewDetails):
    newReview = getReview(reviewId)
    try:
        if newReview:
            newReview.studentId = studentId
            newReview.reviewDetails = reviewDetails
            newReview.userId = userId
            db.session.add(newReview)
            db.session.commit()
            return newReview
    except:
        db.session.rollback()
    return None


'''Delete operations'''

# Get a review based n review ID
# Return false if review not found
# Deletes the review if found and return true
def deleteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
    except:
        db.session.rollback()
    return False


'''Review upvote logic'''

# Gets a review based on review Id
# If review found, increase the upvote score by 1 and return the review
# Return None otherwise
def upvoteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            review.upvoteScore = review.upvoteScore + 1
            db.session.add(review)
            db.session.commit()
            return review
    except:
        db.session.rollback()
    return None


'''Review downvote logic'''

# Gets a review based on review Id
# If review found, increase the downvote score by 1 and return the review
# Return None otherwise
def downvoteReview(reviewId):
    review = getReview(reviewId)
    try:
        if review:
            review.downvoteScore = review.downvoteScore + 1
            db.session.add(review)
            db.session.commit()
            return review
    except:
        db.session.rollback()
    return None
