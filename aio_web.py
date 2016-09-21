#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Stephen Yang'

'''
async web application.
'''

import sys
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.1)
    text = '<h1>Index</h1>'
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def hello(req):
    await asyncio.sleep(0.1)
    name = req.match_info.get('name')
    text = '<h1>hello, %s!</h1>' % ('web' if not name or name.strip() == '' else name)
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(lp):
    app = web.Application(loop=lp)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello', hello)
    app.router.add_route('GET', '/hello/', hello)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await lp.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

def main(argv):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

if __name__ == '__main__':
    main(sys.argv[1:])