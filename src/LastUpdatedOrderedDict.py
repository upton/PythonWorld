#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
        
if __name__ == '__main__':
    lud = LastUpdatedOrderedDict(3)
    lud['a'] = 1
    lud['b'] = 2
    lud['c'] = 3
    lud['b'] = 4
    lud['d'] = 5
    
    print lud
        
