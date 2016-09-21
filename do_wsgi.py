#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(env, resp):
    resp('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello %s!</h1>' % (env['PATH_INFO'][1:] or 'Web')
    return [body.encode('utf-8')]

def main():
    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
     main()
