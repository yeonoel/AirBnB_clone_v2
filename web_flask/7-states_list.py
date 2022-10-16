#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask
from models.state import State
from flask import Flask
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """a HTML page template at the route /states_list."""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
