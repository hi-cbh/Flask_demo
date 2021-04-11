''':cvar
多对多的表的创建
'''
import pymysql # 调用mysql 需要运行这两行代码
pymysql.install_as_MySQLdb()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()
URI="mysql://root:123456@localhost:3306/flaskdatabase?charset=utf8"
engine = create_engine(URI)

# 多对多关联通过第三张表关联，sqlalchemy要自己创建第三张表
class Girl(Base):
    __tablename__ = "girls"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    g2b = relationship("Boy", backref="b2g", secondary="hotels")


class Boy(Base):
    __tablename__ = "boys"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True)
    boy_id = Column(Integer, ForeignKey("boys.id"), nullable=False)
    girl_id = Column(Integer, ForeignKey("girls.id"), nullable=False)


Base.metadata.create_all(engine)