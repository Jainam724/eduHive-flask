# # from prac import web, db  

# # with web.app_context():
# #     db.create_all()

from backend import web, db, Faculty  # Adjust import as per your project structure

with web.app_context():  # Important: Needed to access app context outside routes
    db.create_all()  # Create tables if not exist

    # Create static faculty entries
    faculty1 = Faculty(username="suhani", email="suhani@example.com", password="suhani123", department="Computer Engineering")
    faculty2 = Faculty(username="raj", email="raj@example.com", )

    # Add and commit to database
    db.session.add(faculty1)
    db.session.add(faculty2)
    db.session.commit()

    print("Static faculty data inserted successfully.")



# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from datetime import timedelta

# app = Flask(__name__)
# app.secret_key = "supersecretkey"  # change this in production
# app.permanent_session_lifetime = timedelta(minutes=30)

# # Dummy credentials (replace with DB in future)
# FACULTY_CREDENTIALS = {
#     "faculty@example.com": "password123"
# }

# # Dummy data
# notices = [
#     {
#         'title': 'Exam Schedule Released',
#         'description': 'Mid-sem exams from 25th April.',
#         'department': 'Information and Communication Technology',
#         'semester': '4',
#         'image': 'images/about.jpg'
#     },
#     {
#         'title': 'Workshop on Python',
#         'description': 'Hands-on session on Python.',
#         'department': 'Computer Engineering',
#         'semester': '4',
#         'image': 'images/about.jpg'
#     }
# ]

# resources = [
#     {
#         'subject': 'Python Notes',
#         'semester': '4',
#         'link': 'https://example.com/python-notes'
#     },
#     {
#         'subject': 'DBMS Materials',
#         'semester': '4',
#         'link': 'https://example.com/dbms-notes'
#     }
# ]

# events = [
#     {
#         'title': 'Tech Fest 2025',
#         'date': '2025-05-10',
#         'description': 'Join us for workshops, events, and fun!'
#     },
#     {
#         'title': 'AI Conference',
#         'date': '2025-06-01',
#         'description': 'A seminar on the future of AI.'
#     }
# ]

# # Routes

# @app.route("/")
# @app.route("/index")
# def index():
#     return render_template("index.html")


# @app.route("/e-notice", methods=["GET", "POST"])
# def e_notice():
#     selected_department = request.args.get("department")
#     selected_semester = request.args.get("semester")

#     if selected_department and selected_semester:
#         filtered = [n for n in notices if n["department"] == selected_department and n["semester"] == selected_semester]
#     else:
#         filtered = notices

#     departments = sorted({n["department"] for n in notices})
#     semesters = sorted({n["semester"] for n in notices})

#     return render_template("e_notice.html",
#                            notices=filtered,
#                            departments=departments,
#                            semesters=semesters,
#                            selected_department=selected_department,
#                            selected_semester=selected_semester)


# @app.route("/resources")
# def resources_page():
#     return render_template("resources.html", resources=resources)


# @app.route("/events")
# def events_page():
#     return render_template("events.html", events=events)


# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if email in FACULTY_CREDENTIALS and FACULTY_CREDENTIALS[email] == password:
#             session.permanent = True
#             session["faculty"] = email
#             flash("Login successful!", "info")
#             return redirect(url_for("faculty_dashboard"))
#         else:
#             flash("Invalid email or password", "danger")
#             return redirect(url_for("login"))

#     return render_template("login.html")


# @app.route("/faculty-dashboard")
# def faculty_dashboard():
#     if "faculty" in session:
#         return f"<h2>Welcome {session['faculty']}!</h2><p>Upload/Delete functionality coming soon!</p>"
#     else:
#         flash("Please login first.", "warning")
#         return redirect(url_for("login"))


# @app.route("/logout")
# def logout():
#     session.pop("faculty", None)
#     flash("Logged out successfully", "info")
#     return redirect(url_for("login"))


# if __name__ == "__main__":
#     app.run(debug=True)
