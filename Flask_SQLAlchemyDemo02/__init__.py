# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
# db = SQLAlchemy(app)
#
#
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'flaskdatabase2'
# USERNAME = 'root'
# PASSWORD = '123456'
#
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
#
# SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True
#
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
# app.config["SQLALCHEMY_ECHO"] = SQLALCHEMY_ECHO
#
import pymysql

pymysql.install_as_MySQLdb()