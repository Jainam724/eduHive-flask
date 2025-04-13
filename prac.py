from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

web = Flask(__name__)

web.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/eduhive'
db = SQLAlchemy(web)
web.secret_key = ''
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
    
class enotice(db.Model):
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
    # department = db.Column(db.String(100))
    # semester = db.Column(db.String(20))
    #faculty = db.Column(db.String(100))
    
   
class resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    department = db.Column(db.String(100))
    semester = db.Column(db.String(20))
    faculty = db.Column(db.String(100))

@web.route('/')
@web.route('/home')

def homepage():
    return render_template('index.html')

@web.route('/e-notice', methods=["GET", "POST"]) 
def notice():
    n = enotice.query.filter_by(id='1').first()
    return render_template('e-notice.html', eNotice=n)

@web.route('/e-notice', methods=['GET', 'POST'])
# def enotice():
#     department = request.args.get('department', '')
#     semester = request.args.get('semester', '')
    
#     query = enotice.query.order_by(enotice.date.desc())
    
#     if department:
#         query = query.filter_by(department=department)
#     if semester:
#         query = query.filter_by(semester=semester)
        
#     notices = query.all()
#     return render_template('e-notice.html', notices=notices)

@web.route('/events')
def events():
    return render_template('events.html')

# @web.route('/events')
# def events():
#     events_list = event.query.order_by(event.date.desc()).all()
#     return render_template('events.html', events=events_list)

@web.route('/resources')
def resources():
    return render_template('resources.html')

# @web.route('/resources', methods=['GET', 'POST'])
# def resources():
#     department = request.args.get('department', '')
#     semester = request.args.get('semester', '')
    
#     query = resource.query.order_by(resource.date.desc())
    
#     if department:
#         query = query.filter_by(department=department)
#     if semester:
#         query = query.filter_by(semester=semester)
        
#     resources_list = query.all()
#     return render_template('resources.html', resources=resources_list)

@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/faculty')
def faculty():
    return render_template('faculty.html')

# features add/del

@web.route('/faculty/addnotice', methods=["GET", "POST"])
def addnotice():
    if request.method == "POST":
        title = request.form.get("ntitle")
        desc = request.form.get("ndesc")
        file = request.form.get("nfile")
        date = request.form.get("ndate")
        department = request.form.get("department")
        semester = request.form.get("semester")
        faculty = request.form.get("fname")

        new_notice = enotice(title=title, desc=desc, file=file, date=date, department=department, semester=semester, faculty=faculty)
        db.session.add(new_notice)
        db.session.commit()
        # flash('Notice added successfully!', 'success')
        # return redirect(url_for('addnotice'))
    return render_template('faculty.html')

@web.route('/faculty/delnotice', methods=["GET", "POST"])
def delnotice():
    # if request.method == "POST":
    #     db.session.delete(enotice.query.filter_by(title=request.form.get("title")).first())
    return render_template('delnotice.html')

@web.route('/faculty/addresource', methods=["GET", "POST"])
def addresource():
    if request.method == "POST":
        title = request.form.get("rtitle")
        desc = request.form.get("rdesc")
        file = request.form.get("rfile")
        date = request.form.get("rdate")
        department = request.form.get("department")
        semester = request.form.get("semester")

        new_resource = resource(title=title, desc=desc, file=file, date=date, department=department, semester=semester)
        db.session.add(new_resource)
        db.session.commit()
        flash('Resource added successfully!', 'success')
        return redirect(url_for('addresource'))
    return render_template('addresource.html')

@web.route('/faculty/delresource', methods=["GET", "POST"])
def delresource():
    return render_template('delresource.html')

@web.route('/faculty/addevent', methods=["GET", "POST"])
def addevent():
    if request.method == "POST":
        title = request.form.get("etitle")
        desc = request.form.get("edesc")
        file = request.form.get("efile")
        date = request.form.get("edate")
        # department = request.form.get("department")
        # semester = request.form.get("semester")
        # faculty = request.form.get("fname")

        new_event = event(title=title, description=desc, file=file, date=date)
        db.session.add(new_event)
        db.session.commit()
        flash('Event added successfully!', 'success')
        return redirect(url_for('addevent'))
    return render_template('addevent.html')

@web.route('/faculty/delevent', methods=["GET", "POST"])
def delevent():
    return render_template('delevent.html')

if __name__ == "__main__":
    web.run(debug=True)
