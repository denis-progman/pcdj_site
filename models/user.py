from sqlalchemy import Identity, inspect
from datetime import datetime

from ..enums.continents import Continents

from .. import db # from __init__.py

class User(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at      = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

# Input by User Fields:
    uid_id        = db.Column(db.Integer(), nullable=False, unique=True)
    first_name     = db.Column(db.String(100), nullable=False)
    last_name     = db.Column(db.String(100), nullable=False)
    nickname     = db.Column(db.String(50), nullable=False, unique=True)
    avatar     = db.Column(db.String(256))
    wallpaper     = db.Column(db.String(256))
    preview     = db.Column(db.Text())
    external_link = db.Column(db.String(256))
    continent = db.Column(db.Enum(Continents), nullable=False)
    birthday  = db.Column(db.Date, nullable=False)

# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.email