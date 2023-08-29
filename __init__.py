import logging
import os
from flask import Flask
from .config import config
from db import db, migrate
from flask_sqlalchemy import get_debug_queries

def create_app(config_mode, db, migrate):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app(os.getenv("CONFIG_MODE"), db, migrate)

