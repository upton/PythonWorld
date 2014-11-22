#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle

dd = dict(name='upton', age=18)

with open('dump.dat', 'wb') as f:
    pickle.dump(dd, f)

with open('dump.dat', 'rb') as f:
    d = pickle.load(f)
    print d
