import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_CONNECTION_STRING']
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
