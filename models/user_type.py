from sqlalchemy import Identity
from .main_model import MainModel
from db import db


class UserType(db.Model, MainModel):
    __tablename__ = 'user_types'
    users = db.relationship("UserTypeAssignation", back_populates='user_type', cascade="all, delete")
    track_permissions = db.relationship("TrackPermissionUserTypeAssociation", back_populates='user_type', cascade="all, delete")
    agreements = db.relationship("UserTypeAgreementAssociation", back_populates='user_type', cascade="all, delete")

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True)
    type_name = db.Column(db.String(32), nullable=False, unique=True)
    description = db.Column(db.String(1024))
    icon = db.Column(db.String(256))
