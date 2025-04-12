from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
web = Flask(__name__)

web.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/eduhive'
db = SQLAlchemy(web)
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=True, nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(100))

    def __repr__(self):
        return f'<Faculty {self.username}>'
    
class eNotice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    department = db.Column(db.String(100))
    semester = db.Column(db.String(20))
    faculty = db.Column(db.String(100))

class event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    
   
class resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    department = db.Column(db.String(100))
    semester = db.Column(db.String(20))
    #faculty = db.Column(db.String(100))

@web.route('/')
@web.route('/home')

def homepage():
    return render_template('index.html')

@web.route('/e-notice', methods=["GET", "POST"]) 
def enotice():
    if request.method == "POST":
        selected_department = request.form.get("department")
        selected_semester = request.form.get("semester")
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


#faculty actions

@web.route('/addnotice', methods=["GET", "POST"])
def addnotice():
    return render_template('addnotice.html')

@web.route('/delnotice', methods=["GET", "POST"])
def delnotice():
    return render_template('delnotice.html')

@web.route('/addresource', methods=["GET", "POST"])
def addresource():
    return render_template('addresource.html')

@web.route('/delresource', methods=["GET", "POST"])
def delresource():
    return render_template('delresource.html')

@web.route('/addevent', methods=["GET", "POST"])
def addevent():
    return render_template('addevent.html')

@web.route('/delevent', methods=["GET", "POST"])
def delevent():
    return render_template('delevent.html')

if __name__ == "__main__":
    web.run(debug=True)
