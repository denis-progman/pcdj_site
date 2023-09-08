from sqlalchemy import Identity
from datetime import datetime
from .main_model import MainModel
from db import db


class TrackPermissionUserAssociation(db.Model, MainModel):
    __tablename__ = 'track_permission_user_associations'
    
    track_permission = db.relationship("TrackPermission", back_populates="users")
    user = db.relationship("User", back_populates="track_permissions")
# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    track_permission_id = db.Column(db.Integer(), db.ForeignKey("track_permissions.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)