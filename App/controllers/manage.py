

@manager.command
def make_Student(studentId, firstname, lastname, username, email ):
    Joshua = Student(studentId="816", firstname="Joshua", lastname="Ali", username = "joshuaali", email="joshuaali@hotmail.com")
    try:
        db.session.add(Joshua)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'ERROR: Failed to create student'
    return 'Successfully created student'