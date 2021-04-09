#encoding:utf-8
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from flask import Flask

app = Flask(__name__)
manager = Manager(app)
db = SQLAlchemy(app)
db = SQLAlchemy(use_native_unicode='utf8')

test_data={'user':'lanyue','pass':'lanyue0406'}

def make_shell_context():
    return dict(app=app,db=db,data=test_data)

manager.add_command("shell",Shell(make_context=make_shell_context))

@app.route('/')
def index():
    return '欢迎登录'

if __name__=='__main__':
    manager.run()
