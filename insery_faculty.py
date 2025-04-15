from eduhive_app import db, Faculty, web
from werkzeug.security import generate_password_hash

with web.app_context():
    faculty_list = [
        Faculty(name='Suhani', surname='Mehta', email='suhani@gmail.com', password=generate_password_hash('159357'), method='pbkdf2:sha256', department='Information and Communication Technology'),
        Faculty(name='John', surname='Doe', email='john@example.com', password=generate_password_hash('123456'),method='pbkdf2:sha256', department='ICT'),
        Faculty(name='Jane', surname='Smith', email='jane@example.com', password=generate_password_hash('abcdef'), method='pbkdf2:sha256',department='ICT')
    ]
    db.session.add_all(faculty_list)
    db.session.commit()
    print("Faculty members added successfully!")
