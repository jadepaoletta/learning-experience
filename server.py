from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET']
GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']


@app.route('/', methods=['GET', 'POST'])
def index():
    """Homepage"""

    return render_template("index.html", google_client_id=GOOGLE_CLIENT_ID)

@app.route('/about')
def about():
    """Display the About page"""

    return render_template("about.html")

@app.route('/parents')
def parents():
    """Display the Parents page"""

    return render_template("parents.html")



if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug


    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=9810, host='0.0.0.0')