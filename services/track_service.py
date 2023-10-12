from models.track import Track
from sqlalchemy import select, desc
from db import db
from werkzeug.datastructures import FileStorage
from models.user import User
from models.music_style import MusicStyle
from services.helpers import FileHelper

class TrackService:
    def get_tracks_by(field = None, field_value = None, from_number = None, count = None):
        clauses = []
        if not field == None:
            clauses.append(Track.__dict__[field] == field_value)

        stmt = select(
            Track, User, MusicStyle
        ).join(
            User, isouter=True
        ).join(
            MusicStyle, isouter=True
        ).filter(
            *clauses
        ).order_by(desc(Track.id)).slice(from_number, count)

        response = {}
        for row in db.session.execute(stmt):
            response[row.Track.id] = row.Track.toDict()
            response[row.Track.id]["music_style"] = row.MusicStyle.toDict()
            response[row.Track.id]["user"] = row.User.toDict()
        
        return response
    
    def get_all_tracks(from_number = None, count = None):
        return __class__.get_tracks_by(from_number=from_number, count=count)
    
    def upload_track(file: FileStorage, form: dict): 
        form["wave_url"] = "tmp_wave.url" #tmp replacement
        form["duration"] = 211 #tmp replacement
        form["file_url"] = FileHelper.upload_file(file)

        new_tack = Track()
        for field_name in new_tack.mutable_fields:
            setattr(new_tack, field_name, form.get(field_name, None))
        
        db.session.add(new_tack)
        db.session.commit()

        return __class__.get_tracks_by("id", new_tack.id)[new_tack.id]
    
