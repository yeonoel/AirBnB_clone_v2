#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return string to the root /."""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_h():
    """Return a string to a root /hbnb."""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
