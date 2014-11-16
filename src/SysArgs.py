#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014年11月16日

@author: upton
'''

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world'
    elif len(args) > 1:
        print 'hello %s' % args[1:]
        
if __name__ == '__main__':
    test()
