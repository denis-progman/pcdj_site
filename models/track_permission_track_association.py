from sqlalchemy import Identity
from datetime import datetime
from .main_model import MainModel
from db import db


class TrackPermissionTrackAssociation(db.Model, MainModel):
    __tablename__ = 'track_permission_track_associations'

    track_permission = db.relationship("TrackPermission", back_populates="tracks")
    track = db.relationship("Track", back_populates="track_permissions")
# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    track_permission_id = db.Column(db.Integer(), db.ForeignKey("track_permissions.id", ondelete="CASCADE"), nullable=False)
    track_id = db.Column(db.Integer(), db.ForeignKey("tracks.id", ondelete="CASCADE"), nullable=False)