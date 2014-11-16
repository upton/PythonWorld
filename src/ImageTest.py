#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014年11月16日

@author: upton
'''

import Image

def thumb():
    im = Image.open('test.png')
    print im.format, im.size, im.mode
    im.thumbnail((100, 100))
    im.save('thumb.png', 'PNG')


if __name__ == '__main__':
    thumb()