#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

with codecs.open('cn.txt', 'r', 'gb2312') as f:
    ss = f.readline()

with codecs.open('ss.txt', 'wb', 'gb2312') as f:
    f.write(u'中文')
    
# 使用with语句操作文件IO是个好习惯，会自动close
# 写入中文需要wb binary，同时Unicode字符串
