from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/contact')
def cotact_page():
    return 'Contact page'



@app.route('/<name>')
def greetings(name):
    return 'Welcome '+name


if __name__ == '__main__':
    app.run(debug = True)