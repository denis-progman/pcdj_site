from flask import Flask
from controllers import UserController

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello world!"},
    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/get_users_by/<field>/<field_value>", "methods": ["GET"], "view_func": UserController.get_users_by},
    {"rule": "/get_user_by_id/<user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)
