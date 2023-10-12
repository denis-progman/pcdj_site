from flask import Flask, send_from_directory
from controllers import UserController
from controllers import TrackController

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello world!"},
    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/get_users_by/<field>/<field_value>", "methods": ["GET"], "view_func": UserController.get_users_by},
    {"rule": "/get_user_by_id/<int:user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<int:user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},
    # Track API
    {"rule": "/get_tracks_by/<field>/<field_value>", "methods": ["GET"], "view_func": TrackController.get_tracks_by},
    {"rule": "/get_all_tracks", "methods": ["GET"], "view_func": TrackController.get_all_tracks},
    {"rule": "/upload_track", "methods": ["POST"], "view_func": TrackController.upload_track},
    {"rule": "/download_track/<filename>", "methods": ["GET"], "view_func": TrackController.download_track},

]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)
