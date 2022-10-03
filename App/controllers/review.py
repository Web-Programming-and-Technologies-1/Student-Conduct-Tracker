from App.models import User, Student, Review
from App.database import db
from sqlalchemy.exc import IntegrityError

# Create operations
def createReview(review, studentId, userId):
    review = Review(review = review, studentId = studentId, userId = userId)
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

def getReview(id, userId):
    try:
        return Review.query.filter_by(id=id, userId=userId).first()
    except:
        return 'ERROR: Failed to get the review'

# Update operations
def updateReview(id, review, userId):
    try:
        newReview = getReview(id, userId)
        newReview.review = review,
        db.session.add(newReview)
        db.session.commit()
    except:
        return 'ERROR: Failed to update the review'

# Delete operations
def delete_review(id, userId):
    try:
        review = getReview(id, userId)
        db.session.delete(review)
        db.session.commit()
    except:
        return'ERROR: Failed to delete the review'