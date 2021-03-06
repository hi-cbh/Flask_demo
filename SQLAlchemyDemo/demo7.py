#https://www.cnblogs.com/zwq-/p/10686691.html
# 高级运用
# from demo1 import Users,engine
# from sqlalchemy.orm import sessionmaker
# from demo3 import Student
#
# Session = sessionmaker(engine)
# db_session = Session()
#
# # 查询数据表操作
# # and or
# from sqlalchemy.sql import and_ , or_,desc
# ret = db_session.query(Users).filter(and_(Users.id > 3, Users.name == 'DragonFire')).all()
# ret = db_session.query(Users).filter(or_(Users.id < 2, Users.name == 'DragonFire')).all()
#
# ret = db_session.query(Users).filter(
#     or_(
#         Users.id < 2,
#         and_(
#             Users.name == 'eric',
#             Users.id > 3
#         ),
#         Users.name != ""
#     )
# )
# print(ret)
# #select * from User where id<2 or (name="eric" and id>3) or extra != ""
#
#
# # 查询所有数据
# r1 = db_session.query(Users).all()
#
# #查询数据 指定查询数据列 加入别名
# r2 = db_session.query(Student.name.label('username'), Student.id).first()
# print(r2.id,r2.username) # 15 NBDragon
#
# # 表达式筛选条件
# r3 = db_session.query(Users).filter(Users.name == "DragonFire").all()
#
# # 原生SQL筛选条件
# r4 = db_session.query(Users).filter_by(name='DragonFire').all()
# r5 = db_session.query(Users).filter_by(name='DragonFire').first()
#
# # 字符串匹配方式筛选条件 并使用 order_by进行排序
# r6 = db_session.query(Student).order_by(Student.name.desc()).all()
# for i in r6:
#     print(i.id,i.name)
#
# #原生SQL查询
# from sqlalchemy.sql import text
# r7 = db_session.query(User).from_statement(text("SELECT * FROM User where name=:name")).params(name='DragonFire').all()
#
# # 筛选查询列
# # query的时候我们不在使用User ORM对象,而是使用User.name来对内容进行选取
# user_list = db_session.query(User.name).all()
# print(user_list)
# for row in user_list:
#     print(row.name)
#
# # 别名映射  name as nick
# user_list = db_session.query(User.name.label("nick")).all()
# print(user_list)
# for row in user_list:
#     print(row.nick) # 这里要写别名了
#
# # 筛选条件格式
# user_list = db_session.query(User).filter(User.name == "DragonFire").all()
# user_list = db_session.query(User).filter(User.name == "DragonFire").first()
# user_list = db_session.query(User).filter_by(name="DragonFire").first()
# for row in user_list:
#     print(row.nick)
#
# # 复杂查询
# from sqlalchemy.sql import text
# user_list = db_session.query(User).filter(text("id<:value and name=:name")).params(value=3,name="DragonFire")
#
# # 查询语句
# from sqlalchemy.sql import text
# user_list = db_session.query(User).filter(text("select * from User id<:value and name=:name")).params(value=3,name="DragonFire")
#
# # 排序 :
# user_list = db_session.query(User).order_by(User.id).all()
# user_list = db_session.query(User).order_by(User.id.desc()).all()
# for row in user_list:
#     print(row.name,row.id)
#
# #其他查询条件
# """
# ret = session.query(User).filter_by(name='DragonFire').all()
# ret = session.query(User).filter(User.id > 1, User.name == 'DragonFire').all()
# ret = session.query(User).filter(User.id.in_(session.query(User.id).filter_by(name='DragonFire'))).all() 子查询
# from sqlalchemy import and_, or_
# ret = session.query(User).filter(and_(User.id > 3, User.name == 'DragonFire')).all()
# ret = session.query(User).filter(or_(User.id < 2, User.name == 'DragonFire')).all()
#
#
#
#
# # 限制
# ret = db_session.query(User)[1:2]
#
# # 排序
# ret = db_session.query(User).order_by(User.name.desc()).all()
# ret = db_session.query(User).order_by(User.name.desc(), User.id.asc()).all()
#
# # 分组
# from sqlalchemy.sql import func
#
# ret = db_session.query(User).group_by(User.extra).all()
# ret = db_session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id)).group_by(User.name).all()
#
# ret = db_session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id)).group_by(User.name).having(func.min(User.id) >2).all()
# """
#
# # 关闭连接
# db_session.close()
#
#
# ret = db_session.query(Student).filter(Student.id.between(1, 3)).all() # between 大于1小于3的
# for i in ret:
#     print(i.id,i.name)
# ret = db_session.query(Student).filter(~Student.id.in_([1,4])).all() # in_([1,3,4]) 只查询id等于1,3,4的
# for i in ret:
#     print(i.id,i.name)
# ret = session.query(User).filter(~User.id.in_([1,3,4])).all() # ~xxxx.in_([1,3,4]) 查询不等于1,3,4的
# # 通配符
# ret = db_session.query(Student).filter(Student.name.like('%e%')).all()
#
#
# ret = db_session.query(Student).filter(~Student.name.like('Z%')).all()
# for i in ret:
#     print(i.id,i.name)
#
#
#
# 高级版更新操作
# from my_create_table import User,engine
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(engine)
# db_session = Session()
#
# #直接修改
# db_session.query(Student).filter(Student.id > 3).update({Student.name: Student.name + "099"}, synchronize_session=False)
# db_session.commit()
#
# db_session.query(Student).filter(Student.id > 3).update({"name": Student.name + "123"}, synchronize_session=False)
# db_session.commit()
#
#
# #在原有值基础上添加 - 1
# db_session.query(User).filter(User.id > 0).update({User.name: User.name + "099"}, synchronize_session=False)
#
# #在原有值基础上添加 - 2
# db_session.query(User).filter(User.id > 0).update({"age": User.age + 1}, synchronize_session="evaluate")
# db_session.commit()