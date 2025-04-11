# from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash
# from flask_sqlalchemy import SQLAlchemy
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this in production

# # Configure upload folder
# UPLOAD_FOLDER = 'static/uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # SQLite DB setup
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhive.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # ---------- DATABASE MODELS ---------- #
# class Notice(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     filename = db.Column(db.String(100))

# class Resource(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     filename = db.Column(db.String(100))
#     category = db.Column(db.String(50))

# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     description = db.Column(db.Text)

# # ---------- ROUTES ---------- #
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/notices')
# def notices():
#     query = request.args.get('q')
#     if query:
#         all_notices = Notice.query.filter(Notice.title.ilike(f"%{query}%")).all()
#     else:
#         all_notices = Notice.query.all()
#     return render_template('notices.html', notices=all_notices, query=query)

# @app.route('/resources')
# def resources():
#     query = request.args.get('q')
#     category = request.args.get('category')
#     resources_query = Resource.query

#     if query:
#         resources_query = resources_query.filter(Resource.title.ilike(f"%{query}%"))
#     if category:
#         resources_query = resources_query.filter(Resource.category == category)

#     all_resources = resources_query.all()
#     categories = db.session.query(Resource.category).distinct()
#     return render_template('resources.html', resources=all_resources, query=query, category=category, categories=categories)

# @app.route('/events')
# def events():
#     query = request.args.get('q')
#     if query:
#         all_events = Event.query.filter(Event.title.ilike(f"%{query}%")).all()
#     else:
#         all_events = Event.query.all()
#     return render_template('events.html', events=all_events, query=query)

# @app.route('/about')
# def about():
#     return render_template('about.html')

# # ---------- AUTH SYSTEM FOR FACULTY ---------- #
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'faculty' and password == 'password':  # Change for production
#             session['user'] = username
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials')
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('index'))

# @app.route('/dashboard')
# def dashboard():
#     if 'user' in session:
#         return render_template('dashboard.html')
#     return redirect(url_for('login'))

# # ---------- UPLOAD & DELETE ---------- #
# @app.route('/upload/<item>', methods=['GET', 'POST'])
# def upload(item):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         title = request.form['title']
#         file = request.files.get('file')

#         if item in ['notice', 'resource'] and file:
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)

#             if item == 'notice':
#                 db.session.add(Notice(title=title, filename=filename))
#             elif item == 'resource':
#                 category = request.form['category']
#                 db.session.add(Resource(title=title, filename=filename, category=category))
#             db.session.commit()
#             return redirect(url_for('dashboard'))

#         elif item == 'event':
#             description = request.form['description']
#             db.session.add(Event(title=title, description=description))
#             db.session.commit()
#             return redirect(url_for('dashboard'))

#     return render_template('upload.html', item=item)

# @app.route('/delete/<item>/<int:id>')
# def delete(item, id):
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     model_map = {'notice': Notice, 'resource': Resource, 'event': Event}
#     model = model_map.get(item)
#     if not model:
#         return redirect(url_for('dashboard'))

#     record = model.query.get_or_404(id)
#     if hasattr(record, 'filename'):
#         try:
#             os.remove(os.path.join(app.config['UPLOAD_FOLDER'], record.filename))
#         except FileNotFoundError:
#             pass

#     db.session.delete(record)
#     db.session.commit()
#     return redirect(url_for('dashboard'))

# # ---------- DOWNLOAD ---------- #
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# # ---------- RUN ---------- #
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)