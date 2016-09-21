#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def main():
    print('Test: 010-12345')
    m = re.match(r'^(\d{3})-(\d{5})$', '010-12345')
    print(m.groups())

    t = '19:43:24'
    t = '09:5:8'
    t = '9:03:04'
    t = ' 23:53:04 '
    ts = t.strip()
    print('Test: ', t)
    m = re.match('^([01][0-9]|2[0-3]|[0-9])\:([0-5][0-9]|[0-9])\:([0-5][0-9]|[0-9])$', ts)
    if m == None:
        print('No match!')
    else:
        print(m.groups())

if __name__ == '__main__':
    main()
