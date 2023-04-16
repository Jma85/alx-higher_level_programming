#!/usr/bin/python3
'''
contains the function write_file()
'''


def write_file(filename="", text=""):
    ''' a function that writes a string to a text'''
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
