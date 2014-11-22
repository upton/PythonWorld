#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dd = dict(age=18, x=123, name='upton', b=5, c='xyz',)

s = json.dumps(dd)  

print s
print json.dumps(dd, separators=(',', ':'))  # 去掉，：后面的空格
print json.dumps(dd, indent=2, sort_keys=True)  # 格式美化输出

d = json.loads(s)

print d['name']

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
stu = Student('Bob', 20, 88)

print json.dumps(stu, default=lambda obj: obj.__dict__)
