from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
@make_emphasis
@make_bold
@make_underlined
def hello_world():
    return 'Hello, World!!!'

@app.route('/bye')
@make_underlined
@make_bold
def bye():
    return 'Bye'

if __name__ == "__main__":
    app.run()

# export FLASK_APP=main.py
