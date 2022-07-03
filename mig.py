from app.models.db.member import Member, User
from app.models.db.shared import db
from flask import Flask
import config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate = Migrate(app, db)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()