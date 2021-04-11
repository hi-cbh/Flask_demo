'''
创建外键关联的表结构：
'''
import pymysql # 调用mysql 需要运行这两行代码
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

URI="mysql://root:123456@localhost:3306/flaskdatabase?charset=utf8"
engine = create_engine(URI)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    sch_id = Column(Integer,ForeignKey("school.id"))  # 关联的表的字段,表间的关系
    stu2sch = relationship("School",backref="sch2stu")  # 写在哪边那边就是正向查询，对象间的关系，backref(反向查询)

class School(Base):
    __tablename__ = "school"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)

Base.metadata.create_all(engine)