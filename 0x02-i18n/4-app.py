#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Config class to store app configuration
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply the config to the app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is in the request arguments
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Default to the best match using the previous behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('index.html', 
                           home_title=_("home_title"), 
                           home_header=_("home_header"))

if __name__ == '__main__':
    app.run(debug=True)

