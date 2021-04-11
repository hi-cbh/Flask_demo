"""
多对多表数据的添加与查询：
"""
from sqlalchemy.orm import sessionmaker
from demo5 import engine
from demo5 import Girl,Boy

Session = sessionmaker(engine)
db_session = Session()

print("1.1 增加数据 正向添加")
# 1.增加数据
# relationship 正向添加
g = Girl(name="ZLY",g2b=[Boy(name="ZWQ"),Boy(name="FSF")])
db_session.add(g)
db_session.commit()

print("1.2 增加数据 反向添加")
# relationship 反向添加
b = Boy(name="ZS")
b.b2g = [Girl(name="罗玉凤"),Girl(name="娟儿"),Girl(name="芙蓉姐姐")]
db_session.add(b)
db_session.commit()

print("2 查询 正向")
# 2.查询
# relationship 正向
res = db_session.query(Girl).all()
for g in res:
    for b in g.g2b:
        print(g.name,b.name)

print("2 查询 反向")
# relationship 反向
res = db_session.query(Boy).all()
for b in res:
    for g in b.b2g:
        print(b.name,g.name)