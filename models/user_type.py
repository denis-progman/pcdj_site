from sqlalchemy import Identity
from .main_model import MainModel
from db import db


class UserType(db.Model, MainModel):
    __tablename__ = 'user_types'
    users = db.relationship("UserTypeAssignations", back_populates='user_type')

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    type_name = db.Column(db.String(32), nullable=False, unique=True)
    icon = db.Column(db.String(256))
