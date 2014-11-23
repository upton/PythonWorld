#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = r'\d'

test = '3'
if re.match(s, test):
    
    print 'ok'
else:
    print 'failed'
    
# 识别连续的空格，用正则表达式
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.groups()

# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print re_telephone.match('010-12345').groups()