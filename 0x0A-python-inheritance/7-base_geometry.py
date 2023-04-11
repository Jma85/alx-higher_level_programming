#!/usr/bin/python3

'''
contains the class BaseGeometry
'''


class BaseGeometry:
    '''A class with public instance methods area and integer_variable'''

    def area(self):
        '''raises exception when called'''
        raise Exception("area() is nit implemented")

    def integer_validator(self, name, value):
        '''validates the value is an integer greater than 0'''

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must beb greater than 0".format(name))
