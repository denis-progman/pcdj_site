import os
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from configs import current_config

class FileHelper:
    def upload_file(file: FileStorage):
        file_save_name = secure_filename(file.filename)
        file.save(os.path.join(
            current_config.UPLOAD_FOLDER, 
            current_config.TRACK_STORAGE_FOLDER, 
            file_save_name
        ))
        return file_save_name