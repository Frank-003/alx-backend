#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, timezoneselector
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    # 1. Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)  # Validate the timezone
            return timezone
        except UnknownTimeZoneError:
            pass
    
    # 2. Timezone from user settings
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])  # Validate the timezone
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    
    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']

def get_user():
    """Return a user dictionary or None if not found or if login_as is not passed."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """Executed before each request, sets g.user."""
    g.user = get_user()

@app.route('/')
def index():
    if g.user:
        message = _("logged_in_as", username=g.user["name"])
    else:
        message = _("not_logged_in")
    
    return render_template('index.html', 
                           home_title=_("home_title"), 
                           home_header=_("home_header"), 
                           message=message)

if __name__ == '__main__':
    app.run(debug=True)

