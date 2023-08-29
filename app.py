import os
from . import *
from .controllers.user_controller import get_all_users, get_user_by_id, create_user, update_user, delete_user
from flask import request

if __name__ == "__main__":
    app.run()

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/users", methods=['GET'])
def users_method():
    if request.method == 'GET': return get_all_users(db)
    else: return 'Method is Not Allowed'

@app.route("/create_user", methods=['POST'])
def create_user_method():
    if request.method == 'POST': return create_user(db)
    else: return 'Method is Not Allowed'

@app.route("/update_user/<user_id>", methods=['PUT'])
def update_user_method(user_id):
    if request.method == 'PUT': return update_user(db, user_id)
    else: return 'Method is Not Allowed'

@app.route("/delete_user/<user_id>", methods=['DELETE'])
def delete_user_method(user_id):
    if request.method == 'DELETE': return delete_user(db, user_id)
    else: return 'Method is Not Allowed'
    