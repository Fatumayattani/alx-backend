#!/usr/bin/env python3
"""
Module for a basic Flask app with Babel extension.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    """
    Route for the main page.
    Returns:
        Rendered template for 1-index.html.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
