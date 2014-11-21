#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014年11月19日

@author: upton
'''
def run():
    detail = open("detail.vm", "r")
    newDeatil = open("new.vm", "w")
    lines = detail.readlines()

    for line in lines:
        if  not line.isspace():
            newDeatil.write(line)


if __name__ == '__main__':
    run()