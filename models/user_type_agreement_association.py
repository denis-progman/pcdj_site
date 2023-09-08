from sqlalchemy import Identity
from .main_model import MainModel
from db import db

class UserTypeAgreementAssociation(db.Model, MainModel):
    __tablename__ = 'user_type_agreement_associations'
# Auto Generated Fields:
    agreement = db.relationship("Agreement", back_populates="user_types")
    user_type = db.relationship("UserType", back_populates="agreements")

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    agreement_id = db.Column(db.Integer(), db.ForeignKey("agreements.id", ondelete="CASCADE"), nullable=False)
    user_type_id = db.Column(db.Integer(), db.ForeignKey("user_types.id", ondelete="CASCADE"), nullable=False)
