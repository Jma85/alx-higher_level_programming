#!/usr/bin/python3
'''
this contains module of function is_same_class
'''


def is_same_class(obj, a_class):
    ''' return true if obj is the exact same class otherwise false'''
    return (type(obj) == a_class)
