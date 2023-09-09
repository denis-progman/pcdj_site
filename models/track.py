from sqlalchemy import Identity, inspect
from datetime import datetime

from enums.visibility_enum import VisibilityEnum
from .main_model import MainModel
from db import db


class Track(db.Model, MainModel):
    __tablename__ = 'tracks'

    mutable_fields = [
        "user_id",
        "file_url",
        "wave_url",
        "title",
        "author",
        "cover",
        "cover_url",
        "duration",
        "style_id",
        "checked",
        "visibility",
    ]


    user = db.relationship("User", back_populates="tracks")
    style = db.relationship("MusicStyle", back_populates="tracks")
    track_permissions = db.relationship("TrackPermissionTrackAssociation", back_populates="track", cascade="all, delete")

# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)

# Input by User Fields:
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    file_url = db.Column(db.String(512), nullable=False)
    wave_url = db.Column(db.String(512), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    cover = db.Column(db.Integer())
    cover_url = db.Column(db.String(256))
    duration = db.Column(db.Integer(), nullable=False)
    style_id = db.Column(db.Integer(), db.ForeignKey("music_styles.id"), nullable=False)

    checked = db.Column(db.Boolean(), nullable=False, default=False)
    visibility = db.Column(db.Enum(VisibilityEnum), nullable=False, default=VisibilityEnum.all)
