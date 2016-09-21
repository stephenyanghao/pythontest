#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test screen module'

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,w):
        self.__width = w
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        self.__height = h
    @property
    def resolution(self):
        return self.__height * self.__width

def main():
    s = Screen()
    s.width = 1024
    setattr(s, 'height', 768)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
    print('the resolution is:', getattr(s,'resolution'))

if __name__ == '__main__':
    main()
