import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

def create_app(config_mode, db, migrate):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    db.init_app(app)
    migrate.init_app(app, db)

    return app

db = SQLAlchemy()
migrate = Migrate()
app = create_app(os.getenv("CONFIG_MODE"), db, migrate)
