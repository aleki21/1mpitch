from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name])

#Initializing Flask Extensions
bootstrap = Bootstrap(app)
db.init_app(app)

#Registering blueprints
from .main import main as (main_blueprint)
app.register_blueprint(main_blueprint)

return app