#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import *

# 定义User对象:
metadata = MetaData()

User = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(16), nullable=False)
)

# 初始化数据库连接:
engine = create_engine('sqlite://')
conn = engine.connect()
# 初始化表
metadata.create_all(engine)

ins = User.insert().values(id=1, name='upton')

conn.execute(ins)

s = select([User])
result = conn.execute(s) 

for row in result:
    print row
