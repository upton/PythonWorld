#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年3月9日

@author: upton
'''
import ConfigParser


# 设置default值
cf = ConfigParser.SafeConfigParser({'foo2':'Life',
                                    'bar2':'hard'
                                    })
cf.read("server.conf")

# 返回所有的section
s = cf.sections()
print 'section=', s

print 'url=', cf.get('db', 'url', raw=True) % ('127.0.0.1', '3306')

print 'hello=', cf.get('other', 'hello')
print 'hello2=', cf.get('other', 'hello2')
