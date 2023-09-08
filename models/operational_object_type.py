from sqlalchemy import Identity
from .main_model import MainModel
from db import db

class OperationalObjectType(db.Model, MainModel):
    __tablename__ = 'operational_object_types'
    agreements = db.relationship("OperationalObjectTypeAgreementAssociation", back_populates='operational_object_type', cascade="all, delete")

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    type_name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024))
    icon_url = db.Column(db.String(256))