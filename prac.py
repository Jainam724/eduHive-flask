from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask import send_file
import io
from datetime import datetime

web = Flask(__name__)

web.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/eduhive'
db = SQLAlchemy(web)
web.secret_key = ''
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='eduhive'
    )

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), primary_key=True, nullable=False)
    surname = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(12), nullable=False)
    department = db.Column(db.String(30))

    def __repr__(self):
        return f'<Faculty {self.username}>'
    
class Enotice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    desc = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    department = db.Column(db.String(30))
    semester = db.Column(db.String(20))
    faculty = db.Column(db.String(20))

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    file = db.Column(db.String(100))
    date = db.Column(db.String(20))
    
# class Resources(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20))
#     description = db.Column(db.Text)
#     file = db.Column(db.String(100))
#     date = db.Column(db.String(20))
#     department = db.Column(db.String(30))
#     semester = db.Column(db.String(10))
#     faculty = db.Column(db.String(20))

class Resources(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100)) 
    description = db.Column(db.Text) 
    filename = db.Column(db.String(100)) 
    data = db.Column(db.LargeBinary) 
    mimetype = db.Column(db.String(100)) 
    date = db.Column(db.String(20)) 
    department = db.Column(db.String(30)) 
    semester = db.Column(db.String(10)) 
    faculty = db.Column(db.String(20))

@web.route('/')

@web.route('/home')
def homepage():
    return render_template('index.html')

@web.route('/e-notice')
def e_notice():
    return render_template('e-notice.html')

@web.route('/e-notice/show', methods=['GET', 'POST'])
def show_enotices():
    notices = []
    if request.method == 'POST':
        department = request.form.get('department')
        semester = request.form.get('semester')
        # print(department, semester)
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Enotice WHERE department = %s AND semester = %s"
        cursor.execute(query, (department, semester))
        notices = cursor.fetchall()
        conn.close()
    return render_template('e-notice.html', notices=notices)

@web.route('/events')
def events():
        events_list = []
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM events ORDER BY date DESC LIMIT 4"
        cursor.execute(query)
        events_list = cursor.fetchall()
        conn.close()
        # events_list = events.query.order_by(events.date.desc()).all()[0:4]
        return render_template('events.html', events=events_list)

@web.route('/resources')
def resource():
    return render_template('resources.html')

@web.route('/resources/show', methods=['GET', 'POST'])
def show_resource():
    resources = []
    if request.method == 'POST':
        department = request.form.get('department')
        semester = request.form.get('semester')
        faculty = request.form.get('faculty')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        if faculty!= '':
            query = "SELECT * FROM Resources WHERE department = %s AND semester = %s and faculty = %s"
            cursor.execute(query, (department, semester, faculty))
        else:
            query = "SELECT * FROM Resources WHERE department = %s AND semester = %s"
            cursor.execute(query, (department, semester))
        resources = cursor.fetchall()
        print(resources)
        conn.close()

        # resource = Resources.query.get_or_404(id) 
        # return send_file( io.BytesIO(resource.data), download_name=resource.filename, mimetype=resource.mimetype )
    return render_template('resources.html', resources=resources)

@web.route('/resources/view/<int:id>') 
def view_resource(id): 
    resource = Resources.query.get(id)
    print(resource)
    return send_file(io.BytesIO(resource.data), mimetype=resource.mimetype, download_name=resource.filename, as_attachment=False)

@web.route('/resources/download/<int:id>') 
def download_resource(id): 
    resource = Resources.query.get(id)
    print(resource)
    return send_file(io.BytesIO(resource.data), mimetype=resource.mimetype, download_name=resource.filename, as_attachment=True)

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

        new_notice = Enotice(title=title, desc=desc, file=file, date=date, department=department, semester=semester, faculty=faculty)
        db.session.add(new_notice)
        db.session.commit()
        # flash('Notice added successfully!', 'success')
        # return redirect(url_for('addnotice'))
    return render_template('faculty.html')

@web.route('/faculty/delnotice', methods=["GET", "POST"])
def delnotice():
    if request.method == 'POST':
        title = request.form.get("ntitle")
        date = request.form.get("ndate")
        department = request.form.get('department')
        semester = request.form.get('semester')
        faculty = request.form.get('fname')
        # print(department, semester)
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "DELETE FROM Enotice WHERE title = %s AND date = %s AND department = %s AND semester = %s AND faculty = %s"
        cursor.execute(query, (title, date, department, semester, faculty))
        conn.commit()
        conn.close()
    # if request.method == "POST":
    #     db.session.delete(enotice.query.filter_by(title=request.form.get("title")).first())
    return render_template('faculty.html')

@web.route('/faculty/addresource', methods=["GET", "POST"])
def addresource():
    if request.method == "POST": 
        file = request.files['rfile'] 
        title = request.form.get("rtitle") 
        description = request.form.get("rdesc") 
        date = request.form.get("rdate") 
        department = request.form.get("department") 
        semester = request.form.get("semester") 
        faculty = request.form.get("fname")

    new_file = Resources(title=title,description=description,filename=file.filename,data=file.read(),mimetype=file.mimetype,date=date,department=department,semester=semester,faculty=faculty)
    db.session.add(new_file)
    db.session.commit()
        # flash('Resource added successfully!', 'success')
        # return redirect(url_for('addresource'))
    return render_template('faculty.html')

@web.route('/faculty/delresource', methods=["GET", "POST"])
def delresource():
    if request.method == 'POST':
        title = request.form.get("rtitle")
        date = request.form.get("rdate")
        department = request.form.get('department')
        semester = request.form.get('semester')
        faculty = request.form.get('fname')
        # print(department, semester)
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "DELETE FROM Resources WHERE title = %s AND date = %s AND department = %s AND semester = %s AND faculty = %s"
        cursor.execute(query, (title, date, department, semester, faculty))
        conn.commit()
        conn.close()
    return render_template('faculty.html')

@web.route('/faculty/addevent', methods=["GET", "POST"])
def addevent():
    if request.method == "POST":
        title = request.form.get("etitle")
        desc = request.form.get("edesc")
        file = request.form.get("efile")
        date = request.form.get("edate")
        
        new_event = Events(title=title, description=desc, file=file, date=date)
        db.session.add(new_event)
        db.session.commit()
        # flash('Event added successfully!', 'success')
        # return redirect(url_for('addevent'))
    return render_template('faculty.html')

@web.route('/faculty/delevent', methods=["GET", "POST"])
def delevent():
    if request.method == 'POST':
        title = request.form.get("etitle")
        date = request.form.get("edate")
        # print(department, semester)
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "DELETE FROM Events WHERE title = %s AND date = %s"
        cursor.execute(query, (title, date))
        conn.commit()
        conn.close()
    return render_template('faculty.html')

if __name__ == "__main__":
    web.run(debug=True)
