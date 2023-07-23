#!/usr/bin/python3
'''
Script that starts a Flask web application
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display text'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display text for /hbnb router'''
    return 'HBNB'


if __name__ == '__main__':
    '''Entry Point'''
    app.run(host='0.0.0.0', port=5000)
