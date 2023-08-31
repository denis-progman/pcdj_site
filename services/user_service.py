import uuid
from models.user import User
from models.user_type_assignations import UserTypeAssignations
from models.user_type import UserType
from sqlalchemy import select, desc
from db import db

class UserService:
    def get_users_by(field = None, field_value = None, from_number = None, count = None):
        clauses = []
        if not field == None:
            clauses.append(User.__dict__[field] == field_value)

        stmt = select(
            User, UserType, UserTypeAssignations
        ).join(
            User.user_types, isouter=True
        ).join(
            UserTypeAssignations.user_type, isouter=True
        ).filter(
            *clauses
        ).order_by(desc(User.id)).slice(from_number, count)

        response = {}
        type_key = "type_names"
        for row in db.session.execute(stmt):
            response[row.User.id] = row.User.toDict()
            if not hasattr(response[row.User.id], type_key):
                response[row.User.id][type_key] = {}
            if row.UserTypeAssignations:
                response[row.User.id][type_key][row.UserType.type_name] = row.UserTypeAssignations.toDict()

        return response

    def get_user_by_id(user_id):
        return __class__.get_users_by("id", user_id)[int(user_id)]

    def create_user(request_body):
        new_user = User()
        new_user.uid_id = uuid.uuid4().int >> 100  # tpm for uid service

        for field_name in new_user.mutable_fields:
            setattr(new_user, field_name, request_body.get(field_name, None))
        
        db.session.add(new_user)
        basic_user_type = UserType.query.filter_by(type_name="listener").first()
        basic_user_type_assignations = UserTypeAssignations(
            type_id = basic_user_type.id,
            user_id = new_user.id,
        )
        db.session.add(basic_user_type_assignations)
        db.session.commit()

        return __class__.get_user_by_id(new_user.id)

    def update_user(user_id, request_body):
        user = User.query.get(user_id)

        for field_key, field_value in request_body.items():
            setattr(user, field_key, field_value)
        db.session.commit()

        return __class__.get_user_by_id(user_id)


    def delete_user(user_id):
        user = User.query.get(user_id)
        if user == None:
            return ('User with Id "{}" is not found!').format(user_id)

        db.session.delete(user)
        db.session.commit()
        return ('User with Id "{}" deleted successfully!').format(user_id)
