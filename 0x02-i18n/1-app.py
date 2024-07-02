#!/usr/bin/env python3
""" Babel flask app with Config class"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """ Class Config defintion"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home() -> str:
    """ home route method definition"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
