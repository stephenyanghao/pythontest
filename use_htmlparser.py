#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

URL = 'https://www.python.org/events/python-events/'

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

def main():
    hf = request.urlopen(URL)
    data = hf.read()
    print('Status:',hf.status, hf.reason)
    parser = MyHTMLParser()
    parser.feed(str(data))

if __name__ == '__main__':
    main()
