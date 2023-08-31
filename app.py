import os
from db import db, migrate
from flask import Flask
from configs import config_dict 
from router import routs_init

app_instance = Flask(__name__)
app_instance.config.from_object(config_dict[os.getenv("CONFIG_MODE")])
db.init_app(app_instance)
migrate.init_app(app_instance, db)

if __name__ == "__main__":
    app_instance.run()

routs_init(app_instance)
