#!/usr/bin/env python3
""" Babel flask app with Config class"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Optional


app = Flask(__name__)


class Config():
    """ Class Config defintion"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home() -> str:
    """ home route method definition"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """ get locale definition as localselector for babel"""
    locale_value = request.args.get('locale')
    if locale_value and locale_value in app.config['LANGUAGES']:
        return locale_value
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
