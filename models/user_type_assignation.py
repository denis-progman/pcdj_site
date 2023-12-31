from sqlalchemy import Identity
from datetime import datetime
from .main_model import MainModel
from db import db


class UserTypeAssignation(db.Model, MainModel):
    __tablename__ = 'user_type_assignations'
# Auto Generated Fields:
    user_type = db.relationship("UserType", back_populates="users")
    user = db.relationship("User", back_populates="user_types")

    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    type_id = db.Column(db.Integer(), db.ForeignKey("user_types.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    canceled_at = db.Column(db.DateTime(timezone=True))
    checked = db.Column(db.Boolean, unique=False, default=False)
