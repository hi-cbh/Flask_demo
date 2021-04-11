# import click
#
# from sayhello import app
# from flask_sqlalchemy import SQLAlchemy
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:123456@localhost/flaskdatabase"
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#
#     id=db.Column(db.Integer,primary_key=True)
#
#     username=db.Column(db.String(80),unique=True)
#
#     email=db.Column(db.String(120),unique=True)
#
#     def __init__(self,username,email):
#
#         self.username=username
#
#         self.email=email
#
#     def __repr__(self):
#
#         return '<User %r>' %self.username
#
# @app.route('/',methods=['GET', 'POST'])
# def index():
#     return 'return something'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)