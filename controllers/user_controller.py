from services import UserService
from flask import request, jsonify


class UserController:

    def get_users_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(
            UserService.get_users_by(field=field, field_value=field_value, from_number=from_number, count=count)
        )
    
    def get_users():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(
            UserService.get_users_by(from_number=from_number, count=count)
        )
    
    def get_user_by_id(user_id):
        return jsonify(
            UserService.get_user_by_id(user_id=user_id)
        )
    
    def create_user():
        return jsonify(
            UserService.create_user(request_body=request.get_json())
        )
    
    def update_user(user_id):
        return jsonify(
            UserService.update_user(user_id=user_id, request_body=request.get_json())
        )
    
    def delete_user(user_id):
        return jsonify(
            UserService.delete_user(user_id=user_id)
        )