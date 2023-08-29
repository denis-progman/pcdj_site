import logging
import pprint
from flask import request, jsonify
import uuid
from models.user import User
from models.user_type_assignations import UserTypeAssignations
from models.user_type import UserType
from sqlalchemy import select, desc
from alembic import op
import json


def get_all_users(db):
    from_number = request.args.get('from', default=1, type=int)
    count = request.args.get('count', default=100, type=int)

    stmt = select(
        User, UserType, UserTypeAssignations
    ).join(
        User.user_types, isouter=True
    ).join(
        UserTypeAssignations.user_type, isouter=True
    ).order_by(desc(User.id)).slice(from_number, count)

    response = {}
    type_key = "type_names"
    for row in db.session.execute(stmt):
        response[row.User.id] = row.User.toDict()
        if not hasattr(response[row.User.id], type_key):
            response[row.User.id][type_key] = {}
        if row.UserTypeAssignations:
            response[row.User.id][type_key][row.UserType.type_name] = row.UserTypeAssignations.toDict()

    return jsonify(response)


def get_user_by_id(user_id):
    response = User.query.get(user_id).toDict()
    return jsonify(response)


def create_user(db):
    request_form = request.get_json()

    uid_id = uuid.uuid4().int >> 100  # tpm for uid service
    new_user = User(
        uid_id = uid_id,
        first_name = request_form['first_name'],
        last_name = request_form['last_name'],
        nickname = request_form['nickname'],
        avatar = request_form['avatar'],
        wallpaper = request_form['wallpaper'],
        preview = request_form['preview'],
        external_link = request_form['external_link'],
        continent = request_form['continent'],
        birthday = request_form['birthday'],
    )
    db.session.add(new_user)
    basic_user_type = UserType.query.filter_by(type_name="listener").first()
    basic_user_type_assignations = UserTypeAssignations(
        type_id = basic_user_type.id,
        user_id = new_user.id,
    )
    db.session.add(basic_user_type_assignations)
    db.session.commit()

    return jsonify(basic_user_type_assignations.toDict())


def update_user(db, user_id):
    request_form = request.get_json()
    user = User.query.get(user_id)

    for field_key, field_value in request_form.items():
        setattr(user, field_key, field_value)
    db.session.commit()

    response = User.query.get(user_id).toDict()
    return jsonify(response)


def delete_user(db, user_id):
    user = User.query.get(user_id)
    if user == None:
        return ('User with Id "{}" is not found!').format(user_id)

    user.delete()
    db.session.commit()
    return ('User with Id "{}" deleted successfully!').format(user_id)
