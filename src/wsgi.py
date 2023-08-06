import os
import sys

sys.path.insert(0, os.getcwd())

from src import create_app, db


application = create_app(config_name="production")
with application.app__context():
db.create_all()
