from sqlalchemy import Identity
from .main_model import MainModel
from db import db


class MusicStyle(db.Model, MainModel):
    __tablename__ = 'music_styles'
    tracks = db.relationship("Track", back_populates="style")

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    style_name = db.Column(db.String(64), nullable=False, unique=True)
    icon = db.Column(db.String(256))