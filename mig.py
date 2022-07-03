# !!! This file is used purely for migration !!!
# !!! All new added models need to be imported in the line:
# !!! from app.models.db.member import Member, User, ...
# !!! Migration steps:
# !!! flask db migrate FLASK_APP=mig.py
# !!! flask db upgrade -m "migration update message"

# External 
from flask import Flask
import config
from flask_migrate import Migrate

# Internal
from app.models.db.member import Member, User
from app.models.db.shared import db


def create_app():
    db_instance = db.getInstance()

    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db_instance().init_app(app)
    migrate = Migrate(app, db_instance)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()