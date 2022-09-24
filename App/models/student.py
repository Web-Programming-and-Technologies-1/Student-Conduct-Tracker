from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Student(db.Model):
    studentId = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(50), nullable=False)
    lastname =  db.Column(db.String(50), nullable=False)
    username =  db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    karmaScore = db.Column(db.Integer)

    def __init__(self, firstname, lastname, username, email, karmaScore):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.karmaScore = karmaScore

    def toDict(self):
        return{
            'id': self.studentId,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
            'karmascore': self.karmaScore
        }

    
