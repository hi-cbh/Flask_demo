'''
单表的增删改查：
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from demo1 import Users # 调用User对象

# 创建引擎
print("创建引擎")
URI="mysql://root:123456@localhost:3306/flaskdatabase?charset=utf8"
engine = create_engine(URI)
Session = sessionmaker(engine)
db_session = Session()

print("1. 增加数据add(创建表结构的类名(字段名=添加的数据))")
# 1. 增加数据add(创建表结构的类名(字段名=添加的数据))
db_session.add(Users(name="ZWQ"))  # 相当于建立一条添加数据的sql语句
db_session.commit()  # 执行
db_session.close()   # 结束关闭

print("1.1 批量添加")
# 批量添加
db_session.add_all([Users(name="清风徐来"), Users(name="水波不兴")])
db_session.commit()
db_session.close()

print("2.查询 query(表结构的类名)")
# 2.查询 query(表结构的类名)
sqlres = db_session.query(Users)
print(sqlres)  # 直接翻译输出对应的SQL查询语句

print("2.1 返回表中所有数据对象")
res = db_session.query(Users).all()  # 返回表中所有数据对象
print(res)# [<creatTable.Users object at 0x00000000038A1B00>,<creatTable.Users object at 0x00000000038A1B70>]

for u in res:
    print(u.id, u.name)

print("2.2 取第一个，返回是对象")
res = db_session.query(Users).first()  # 取第一个，返回是对象
print(res.id, res.name)

print("2.3 返回符合条件查询结果")
res = db_session.query(Users).filter(Users.name == "ZWQ").first()  # 返回符合条件查询结果
print(res.id)

print("2.4 filter中的条件可以是模糊条件,多个条件")
res = db_session.query(Users).filter(Users.id <= 1000, Users.name == "ZWQ").all() # filter中的条件可以是模糊条件,多个条件
for u in res:
    print(u.id,u.name)

print("3.更改数据")
# 3.更改数据 update({k:v})
res = db_session.query(Users).filter(Users.name == "ZWQ").first()  # 返回符合条件查询结果
res = db_session.query(Users).filter(Users.id == res.id).update({"name":"DragonFire"})
print(res)
db_session.commit()

print("3.1 全部修改，返回修改的数据个数")
res = db_session.query(Users).update({"name":"ZWQ"})  # 全部修改，返回修改的数据个数
print(res)
db_session.commit()

print("4.删除 delete()结合查询条件删除")
# 4.删除 delete()结合查询条件删除
res = db_session.query(Users).filter(Users.id == 1).delete()  # 删除否合条件的数据，返回删除数量
print(res)
db_session.commit()

print("4.1 删除表中所有数据，返回删除数量")
res = db_session.query(Users).delete()  # 删除表中所有数据，返回删除数量
print(res)
db_session.commit()