from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class (Userdb.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), unique=True, nullable=False)
    firstname =  db.Column(db.String(50), nullable=False)
    lastname =  db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    staff = db.relationship('Staff', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.staffId,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

  


