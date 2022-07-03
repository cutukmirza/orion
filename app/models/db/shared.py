from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config



# singleton class for db 
class DB:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if DB.__instance == None:
         DB()
      return DB.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if DB.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         DB.__instance = SQLAlchemy(engine_options={"pool_size": 15, "max_overflow": 35})

# singleton class for Flask Server 
class Server:
    __instance = None
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Server.__instance == None:
         Server()
      return Server.__instance
    def __init__(self):
      """ Virtually private constructor. """
      if Server.__instance != None:
         raise Exception("This class is a singleton!")
      else:
        Server.__instance = Flask(__name__)
    def set_config(self, config):
        self.__instance.config.from_object(config)



db = DB()
server = Server()
server.set_config(config.DevelopmentConfig)
db.getInstance().init_app(server.getInstance())