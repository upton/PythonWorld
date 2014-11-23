#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

natuals = itertools.count(1)
for n in natuals:
    print n
    if n == 100:
        break

cycle = itertools.cycle(range(1, 11))
i = 0
for n in cycle:
    print n
    i += 1
    if i == 100:
        break
    
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)  # 为什么这里要用list()函数呢？

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x

# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：

r = map(lambda x: x * x, [1, 2, 3])
print r  # r已经计算出来了

    
    
