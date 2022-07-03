from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy(engine_options={"pool_size": 15, "max_overflow": 35})
server = Flask(__name__)