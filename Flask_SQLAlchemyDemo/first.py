from app import db
from models import *
# 原生sql语句操作
sql = 'select * from user'
result = db.session.execute(sql)

# 查询全部
User.query.all()
# 主键查询
User.query.get(1)
# 条件查询
# User.query.filter_by(User.username='name')
# 多条件查询
from sqlalchemy import and_
User.query.filter_by(and_(User.username =='name',User.password=='passwd'))
# 比较查询
User.query.filter(User.id.__lt__(5)) # 小于5
User.query.filter(User.id.__le__(5)) # 小于等于5
User.query.filter(User.id.__gt__(5)) # 大于5
User.query.filter(User.id.__ge__(5)) # 大于等于5
# in查询
User.query.filter(User.username.in_('A','B','C','D'))
# 排序
User.query.order_by('age') # 按年龄排序，默认升序，在前面加-号为降序'-age'
# 限制查询
User.query.filter(age=18).offset(2).limit(3)  # 跳过二条开始查询，限制输出3条

# # 增加
# use = User(id,username,password)
# db.session.add(use)
# db.session.commit()

# 删除
# User.query.filter_by(User.username='name').delete()

# 修改
# User.query.filter_by(User.username='name').update({'password':'newdata'})