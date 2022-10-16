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


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Return string following by value of text."""
    x = text.replace("_", " ")
    return ("C " + x)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_p(text="is cool"):
    """ Return “Python ”, followed by the value of the text."""
    text = text.replace("_", " ")
    return ("Python %s" % text)


@app.route('/number/<int:n>', strict_slashes=False)
def hello_n(n):
    """ Return “n is a number” only if n is an integer."""
    return ("%s is a number" % n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
