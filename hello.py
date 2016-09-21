#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'
__author__ = 'Stephen Yang'

import sys

def main():
    args = sys.argv
    args_len = len(args)
    if args_len == 1:
        print('Hello world!')
    elif args_len == 2:
        print('Hello %s!'%args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    main()
