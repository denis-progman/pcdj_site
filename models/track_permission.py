from sqlalchemy import Identity
from datetime import datetime
from .main_model import MainModel
from db import db


class TrackPermission(db.Model, MainModel):
    __tablename__ = 'track_permissions'

    tracks = db.relationship("TrackPermissionTrackAssociation", back_populates="track_permission")
    user_types = db.relationship("TrackPermissionUserTypeAssociation", back_populates="track_permission")
    users = db.relationship("TrackPermissionUserAssociation", back_populates="track_permission")
    agreement = db.relationship("Agreement", back_populates="track_permissions")

# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)

# Input by User Fields:
    track_id = db.Column(db.Integer(), db.ForeignKey("tracks.id", ondelete="CASCADE"), nullable=False)
    agreement_id = db.Column(db.Integer(), db.ForeignKey("agreements.id", ondelete="CASCADE"), nullable=False)
    canceled_at = db.Column(db.DateTime(timezone=True))
