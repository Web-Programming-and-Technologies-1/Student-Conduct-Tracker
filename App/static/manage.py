from App.models import  User, Review, Student
from App.database import db
from sqlalchemy.exc import IntegrityError

@manager.command
def make_user():
    Joshua = Student(studentId="816", firstname="Joshua", lastname="Ali", username = "joshuaali", email="joshuaali@hotmail.com")
    
        db.session.add(Joshua)
        db.session.commit()
        print("users created")

if __name__ == "__main__":
    manager.run()
    