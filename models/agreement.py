from sqlalchemy import Identity
from datetime import datetime
from .main_model import MainModel
from db import db


class Agreement(db.Model, MainModel):
    __tablename__ = 'agreements'

    mutable_fields = [
        "agreement_name",
        "description",
        "icon_url",
        "agreement_text"
    ]

    user_types = db.relationship("UserTypeAgreementAssociation", back_populates='agreement', cascade="all, delete")
    operational_object_types = db.relationship("OperationalObjectTypeAgreementAssociation", back_populates='agreement', cascade="all, delete")
    track_permissions = db.relationship("TrackPermission", back_populates='agreement', cascade="all, delete")

# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
# Input by User Fields:
    agreement_name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(512))
    icon_url = db.Column(db.String(256), nullable=False)
    agreement_text = db.Column(db.Text())
    agreement_url = db.Column(db.String(256))