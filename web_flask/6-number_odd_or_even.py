#!/usr/bin/python3
'''
Script that starts a Flask web application
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display text'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display text for /hbnb router'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    '''Function for a variable route'''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonrt(text='is cool'):
    '''Function for python route and sub directories'''
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Function for routing the url with "number" after root'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    '''Function to return templates/5-number.html if n is an int'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''
    Function to check whether a number is odd or even
    Then returns Jinja template based on value n
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    '''Entry Point'''
    app.run(host='0.0.0.0', port=5000)
