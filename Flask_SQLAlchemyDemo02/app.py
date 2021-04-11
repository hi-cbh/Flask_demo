#
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
#
#
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#
#

# -*- coding:utf-8 -*-
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost:3306/flaskdatabase2?charset=utf8"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)


class Role(db.Model):

    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    users = db.relationship('User',backref="role")
    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s" % (self.id,self.name)


class User(db.Model):
    # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(16))
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User: %s %s %s %s" % (self.id,self.name,self.password,self.role_id)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email":self.email,
            "password": self.password

        }


@app.route('/')
def hello_world():
    user = User.query.get(1)
    return jsonify(user.to_json()) , 200

if __name__ == '__main__':
    # 删除所有的表
    db.drop_all()
    # 创建表
    db.create_all()

    ro1 = Role(name = "admin")
    # 先将ro1对象添加到会话中，可以回滚。
    db.session.add(ro1)

    '''
        在执行 db.session.commit() 提交到数据库出错时，需要执行数据库回滚，保证后续操作正常。
        try: 
            .
            .
        except Exception as e:
            db.session.rollback() # 执行数据库回滚
    '''

    try:
        ro2 = Role()
        ro2.name = 'user'
        db.session.add(ro2)
        # 最后插入完数据一定要提交
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    try:
        us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
        us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
        us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
        us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
        us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
        us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
        us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
        us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
        us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
        us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
        db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    app.run(debug=True)