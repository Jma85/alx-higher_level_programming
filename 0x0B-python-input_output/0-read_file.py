#!/usr/bin/python3
'''contains the read_file function'''


def read_file(filename=""):
    ''' reads atext file(UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding="utf-8") as f:
            print(f.read(), end="")
