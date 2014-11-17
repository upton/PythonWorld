#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014年11月16日

@author: upton
'''

class User(object):
    '''
    User class
    '''

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name = value
       
    @property 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    
    def __len__(self):
        return 100
    def __str__(self):
        return 'Name:%s, age:%s' % (self.__name, self.__age)
    
    def userView(self):
        print '%s\'s age is %s' % (self.__name, self.__age)
        
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    def __call__(self):
        print 'path=%s' % self._path
        
if __name__ == '__main__':
    upton = User('upton', 18)
    louis = User('louis', 7)
    upton.userView()
    louis.userView()
    
    upton.score = 99
    
    print upton.score
    
    upton.set_name('upton chen')
    print upton.get_name()
    
    print dir(upton)
    print len(upton)
    
    print hasattr(upton, 'score')
    print getattr(upton, 'score')
    
    upton.name = 'Upton Chen'
    print upton.name
    
    print Chain().status.user.list
    
    cc = Chain().status
    cc()

    print callable(cc)