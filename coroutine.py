#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    cr = ''
    while True:
        cn = yield cr
        if not cn:
            return
        print('[CONSUMER] Consuming %s...' % cn)
        cr = str(cn) + ' OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def main():
    c = consumer()
    produce(c)

if __name__ == '__main__':
    main()
