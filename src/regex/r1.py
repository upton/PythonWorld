#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年3月9日

@author: upton
'''
import re

pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'hell')
result3 = re.match(pattern, 'hello w')
result4 = re.match(pattern, 'hello!')

print result1.group()
print result2
print result3.group()
print result4.group()



print '==================='

# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<id>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')


print '------------------------'

print re.search('world', 'hello world test world').group()

print '-----------------------'
pattern = re.compile(r'\d+')
print 'split:', re.split(pattern, 'one1two2three3four4')

print '-----------------------'
pattern = re.compile(r'\d+')
print 'findall', re.findall(pattern, 'one1two2three3four4')

print '-----------------------'
pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print m.group(),
    
print '-----------------------'
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print re.sub(pattern, r'\2 \1', s)
 
def foo(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.sub(pattern, foo, s)

print '-----------------------'

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print re.subn(pattern, r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print re.subn(pattern, func, s)
 
### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)

ss = '''{dfg:mon,abc: 123,  xyz1 : aaa  ,key :value1 } '''

pattern = re.compile(r'\s*([A-Za-z]\w+?)\s*:\s*(\w+)\s*')

print pattern.sub(r'"\1":"\2"', ss)

