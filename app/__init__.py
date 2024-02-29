from flask import Flask
from flask_mail import Mail


# Initialize Flask app
app = Flask(__name__, static_folder=r"C:\Users\Ousskh\Desktop\analytica\app\static")

# Import mail configuration from config.py
app.config.from_object('app.config')

# Initialize Flask-Mail
mail = Mail(app)

# Import routes after initializing app to avoid circular import
from app import routes

wsgi_app = app.wsgi_app



