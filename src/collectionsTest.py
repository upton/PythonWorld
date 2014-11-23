#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print p

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

dd = defaultdict(lambda: 'N/A..')
dd['key1'] = 'abc'

print dd['key1']  # key1存在
print dd['key2']  # key2不存在，返回默认值

d = dict([('a', 1), ('c', 2), ('b', 3)])
print d  # dict的Key是无序的

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict的Key是有序的
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print c

