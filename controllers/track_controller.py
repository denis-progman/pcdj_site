from services import TrackService
from flask import request, jsonify

class TrackController:
    def get_tracks_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(
            TrackService.get_tracks_by(field=field, field_value=field_value, from_number=from_number, count=count)
        )
    
    def upload_track():
        track_file = request.files["track"]
        return jsonify(
            TrackService.upload_track(track_file, request.form.to_dict())
        )
