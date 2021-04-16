''':cvar
项目初始化，上下文关联
'''
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_bootstrap import Bootstrap
from flask_moment import Moment
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@106.13.223.228:3308/flaskdatabase?charset=utf8"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123456"
# 创建数据库的操作对象
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


from Flask_SQLAlchemyDemo02 import models, forms, views