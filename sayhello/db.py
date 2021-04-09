from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os



app=Flask('Flask_demo')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   #
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL"
                                                  ,"sqlite:///C:\Users\Administrator\IdeaProjects\sayhello\data.db")

db = SQLAlchemy(app)




