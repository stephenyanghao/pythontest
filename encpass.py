#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
salt = '`saLt-Added'

def encpass(user,passwd):
    if not isinstance(user, str) or not isinstance(passwd, str):
        return None
    s = salt + user + passwd
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def main():
    user = 'yanghao'
    passwd = '123455'
    encs = encpass(user, passwd)
    print('user=<%s>,pass=<%s>, enc=<%s>.'%(user, passwd, encs))

if __name__ == '__main__':
    main()
