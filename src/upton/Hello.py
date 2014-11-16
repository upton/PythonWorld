#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import functools

strs = r'''dgfdf\ghj\\gfh\n
    cfdfgdfg\\n
\n
'''

print len(strs)  

print 3 > 2

nn = None

print 'hi %s, nice to meet you' % ('阿普顿')

ll = ['a', 1, True]
tt = (1, 2, 3, 4)

ll.append(5)
ll.pop(0)
print len(ll), ll, ll[2], ll[-1]
print ll[:2]
print tt

length = 6
if length > 7:
    print 'aa'
elif length > 5:
    print 'bb'
    print 'b'
else:
    print 'cc'

ff = None
if ff:
    print 'nnn'
    
sumss = 0
for x in range(101):
    sumss += x
print sumss

i = 100

ss = 0
while i > 0:
    ss += i
    i -= 1
    
print ss

score = {'upton':100, 'lexuan':99}
for key in score:
    print key , ':', score[key]
    
print score['upton']
print score.get('lexuan')
print score.get('xx')
print score.get('oo', -1)

ss = set([1, 6, 3, 3, 4])
ss.add(5)
ss.add(2)
ss.remove(1)
print ss

print abs(-1234)

def add(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('bad operand type')
    
    return x + y

def foo(x, y):
    return x + 1, y + 1

print add(1, 2)

print foo(5, 10)
x, y = foo(10, 20)

print x, y

def bar(x, y=2):
    return x + y

print bar(1)
print bar(1, 5)

def add_end(L=[]):
    L.append('END')
    return L

print add_end()  # ['END']
print add_end()  # ['END', 'END']

def add_end2(L=None):  # L默认参数要是不可变对象
    if L == None:
        L = []
        
    L.append('END')
    return L

print add_end2()
print add_end2()


def calc(*numbers):
    sNum = 0
    for n in numbers:
        sNum += n
    return sNum

print calc(1, 2, 3)
print calc(1, 2, 3, 4)
nums = [1, 2, 3, 4, 5]
print calc(*nums)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
    
person('upton', 18, g='m', f=99)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

dd = [x * x for x in range(1, 11)]
print dd

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

def f(x):
    return x * x

print map(f, range(1, 10))

# def fn(x, y):
#     return x * 10 + y
# 
# print reduce(fn, [1, 3, 5, 7, 9]) #= fn(fn(fn(fn(1,3),5),7),9)

def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))

print sorted([1, 8, 6, 0, 3], lambda x, y:y - x)

print os.listdir('.')

def lazy_sum(*args):
    def sums():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sums

fff1 = lazy_sum(1, 2, 3, 4)
fff2 = lazy_sum(5, 6, 7, 8)

print fff1()
print fff2()

print fff1.__name__

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'start call %s%s' % (func.__name__, args)
        vv = func(*args, **kw)
        print 'end call %s with result %s' % (func.__name__, vv)        
        return vv
    return wrapper

@log
def myFunc(x, y=2):
    return x + y

print myFunc.__name__

print myFunc(1)

myFunc5 = functools.partial(myFunc, y=5)
print myFunc5(2)

