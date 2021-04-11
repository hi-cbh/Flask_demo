'''
创建单表结构
'''
import pymysql # 调用mysql 需要运行这两行代码
pymysql.install_as_MySQLdb()

from sqlalchemy.ext.declarative import declarative_base  # 导入基类
from sqlalchemy import create_engine # 打开数据库的连接 -- 创建数据库引擎
from sqlalchemy import Column, Integer, String  # 数据类型

# Base = ORM基类 - 要按照ORM的规则定义你的类
Base = declarative_base()

class Users(Base):
    __tablename__ = "user"
    # 创建ID数据字段 , 那么ID是不是一个数据列呢? 也就是说创建ID字段 == 创建ID数据列
    # id = Column(数据类型,索引,主键,外键,等等)
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    name = Column(String(32), nullable=False)  # nullable=False 不能为空

# 创建数据库引擎
engine = create_engine("mysql://root:123456@localhost:3306/flaskdatabase?charset=utf8")

# Base自动检索所有继承Base的ORM 对象 并且创建所有的数据表
Base.metadata.create_all(engine)
