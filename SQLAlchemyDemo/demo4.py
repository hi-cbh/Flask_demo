""":cvar
外键关联的表添加与查询操作

"""
from sqlalchemy.orm import sessionmaker
from demo3 import engine
from demo3 import Student,School  # 导入创建表结构的类

Session = sessionmaker(engine)
db_session = Session()

print("1.添加数据")
# 1.添加数据
db_session.add(School(name="NCU"))
db_session.commit()

print("1.1 relationship  正向添加 Student为正向表")
# relationship  正向添加
stu = Student(name="清风徐来",stu2sch=School(name="NCU"))
db_session.add(stu)
db_session.commit()

print("1.2 relationship  反向添加")
# relationship  反向添加
sch = School(name="NCU")
sch.sch2stu = [Student(name="YWB"),Student(name="CT")]
db_session.add(sch)
db_session.commit()

print("2.查询 正向跨表")
# 2.查询
res = db_session.query(Student).all()
for stu in res:
    print(stu.name,stu.stu2sch.name)  # 正向跨表

print("查询 反向跨表")
res = db_session.query(School).all()
for sch in res:
    for stu in sch.sch2stu:
        print(sch.name,stu.name)  # 反向跨表