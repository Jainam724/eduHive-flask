from flask import Flask, render_template

web = Flask(__name__, template_folder='frontend')

@web.route('/')
@web.route('/home')

def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    web.run(debug=True)