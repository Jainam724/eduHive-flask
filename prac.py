from flask import Flask, render_template

web = Flask(__name__, template_folder='frontend')

@web.route('/')
@web.route('/home')

def homepage():
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

if __name__ == '__main__':
    web.run(debug=True)