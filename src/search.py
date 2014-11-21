#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def search(keyword, path='.'):
    dirs = [x for x in os.listdir(path) if os.path.isdir(x)]
    files = [x for x in os.listdir(path) if os.path.isfile(x) and keyword in os.path.split(x)[1]]        

    for f in files:
        print os.path.join(os.path.abspath(path), f)
    for d in dirs:
        search(keyword, os.path.join(path, d))
        
    
    
    
    
if __name__ == '__main__':
    keyword = raw_input("please input keyword and Enter to search: ")
    search(keyword)
