from flask import Flask
from random import randint

number = randint(0, 9)
print(number)


app = Flask(__name__)


@app.route('/')
def landing():

    return '<h1>Guess a number between 0 and 9 </h><br><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="" width="250" height="250">'

@app.route('/<int:guess>')
def guess(guess):
    if guess < number:
        return 'too low'
    elif guess > number:
        return ' too high'
    else:
        return '<h1> correct </h1>'


if __name__ == '__main__':
    app.run()

