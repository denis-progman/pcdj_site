import logging
from flask import request, jsonify
import uuid

# from models import db
from ..models.user import User

# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522

def get_all_users():
    accounts = User.query.all()
    response = []
    for account in accounts: response.append(account.toDict())
    return jsonify(response)

def get_user_by_id(user_id):
    response = User.query.get(user_id).toDict()
    return jsonify(response)

def create_user(db):
    request_form = request.get_json()

    uid_id = uuid.uuid4().int >> 96 # tpm for uid service
    new_user = User(
        uid_id             = uid_id,
        first_name          = request_form['first_name'],
        last_name       = request_form['last_name'],
        nickname       = request_form['nickname'],
        avatar        = request_form['avatar'],
        wallpaper        = request_form['wallpaper'],
        preview        = request_form['preview'],
        external_link  = request_form['external_link'],
        continent  = request_form['continent'],
        birthday   = request_form['birthday'],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.toDict())

def update_user(db, user_id):
    request_form = request.form.to_dict()
    user = User.query.get(user_id)

    for field_key, field_value in request_form.iteritems():
        user[field_key] = field_value

    db.session.commit()

    response = User.query.get(user).toDict()
    return jsonify(response)

def delete_user(db, user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return ('User with Id "{}" deleted successfully!').format(user_id)
