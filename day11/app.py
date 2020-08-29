from flask import Flask
from flask import render_template
app = Flask(__name__)




@app.route('/')
def hello_world():
    return render_template('index.html')


# jinja


@app.route('/<nameFlask>')
def greetUser(nameFlask):
    errorFlask = False
    if len(nameFlask)<3:
        errorFlask =True
    return render_template('hello.html', name=nameFlask, error=errorFlask)