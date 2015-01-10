#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil as sh

print os.name
print os.uname()  # Windows上是不能调用的
print os.environ['PATH']
print os.getenv('PATH', '123')
print os.path.abspath('.')

print os.path.join('/Users/michael', 'testdir')  
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。：/Users/michael\testdir

pp = os.path.abspath('.')  # 当前绝对路径

print os.path.split(pp)
print os.path.splitext('/path/to/file.txt')

# newDir = os.path.join(pp, 'newDir')
# if not os.path.exists(newDir):
#     os.mkdir(newDir)
#     
# if os.path.exists(newDir):
#     os.rmdir(newDir)

dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print dirs

# sh.copyfile('cn.txt', 'cn.txt.bak')

py = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
print py


















