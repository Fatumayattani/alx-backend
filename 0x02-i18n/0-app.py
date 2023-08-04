#!/usr/bin/env python3
"""
Module for a basic Flask app.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route for the main page.
    Returns:
        Rendered template for index.html.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
