import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TRACK_STORAGE_FOLDER = "track_storage"
    MAX_CONTENT_LENGTH = 1024 * 1024 * 25 # 25 mb

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")
    UPLOAD_FOLDER = "dev_file_storage"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")

config_dict = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig
}

current_config = config_dict[os.getenv("CONFIG_MODE")]