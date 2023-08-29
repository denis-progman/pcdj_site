from sqlalchemy import Identity, inspect
from datetime import datetime
from .main_model import MainModel
from enums.continents_enum import ContinentsEnum
from db import db


class User(db.Model, MainModel):
    __tablename__ = 'users'
    user_types = db.relationship("UserTypeAssignations", back_populates='user')
# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    uid_id = db.Column(db.Integer(), nullable=False, unique=True)

# Input by User Fields:
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(50), nullable=False, unique=True)
    avatar = db.Column(db.String(256))
    wallpaper = db.Column(db.String(256))
    preview = db.Column(db.Text())
    external_link = db.Column(db.String(256))
    continent = db.Column(db.Enum(ContinentsEnum), nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    # @validates('time_per_unit')
    # def empty_string_to_null(self, key, value):
    #     if isinstance(value, str) and value == '':
    #         return None
    #     else:
    #         return value

    # @classmethod
    # def __declare_last__(cls):
    #     ValidateString(Item.name, False, True, "The name type must be string")
    #     ValidateNumber(Item.price, True, "The price type must be number")
    #     ValidateURL(Item.image_link, True, True, "The image link is not valid")
