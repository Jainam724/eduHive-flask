from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
web = Flask(__name__)

web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhive.db'
db = SQLAlchemy(web)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(100))

    def __repr__(self):
        return f'<Faculty {self.username}>'
    
class eNotice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    department = db.Column(db.String(100))
    semester = db.Column(db.String(20))

class event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.String(20))
    description = db.Column(db.Text)
   
class resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    category = db.Column(db.String(50))
    department = db.Column(db.String(100))
    semester = db.Column(db.String(20))
    # faculty = db.Column(db.String(100))

@web.route('/')
@web.route('/home')

def homepage():
    # faculty = Faculty(username = "suhani", email = "abc@gmail.com")
    # db.session.add(faculty)
    # db.session.commit()
    return render_template('index.html')

@web.route('/e-notice')
def enotice():
    return render_template('e-notice.html')

@web.route('/events')
def events():
    return render_template('events.html')

@web.route('/resources')
def resources():
    return render_template('resources.html')

@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/faculty')
def faculty():
    return render_template('faculty.html')

if __name__ == "__main__":
    web.run(debug=True)
