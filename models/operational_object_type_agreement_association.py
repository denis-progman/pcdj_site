from sqlalchemy import Identity
from .main_model import MainModel
from db import db

class OperationalObjectTypeAgreementAssociation(db.Model, MainModel):
    __tablename__ = 'operational_object_type_agreement_associations'

    operational_object_type = db.relationship("OperationalObjectType", back_populates="agreements")
    agreement = db.relationship("Agreement", back_populates="operational_object_types")
# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    agreement_id = db.Column(db.Integer(), db.ForeignKey("agreements.id", ondelete="CASCADE"), nullable=False)
    operational_object_type_id = db.Column(db.Integer(), db.ForeignKey("operational_object_types.id", ondelete="CASCADE"), nullable=False)
