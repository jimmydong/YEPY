# -*- coding: utf-8 -*-
"""
This is a temp test file
!这不是框架文件！
"""
import test
import bucket
from yepy import test

class Test():
    count = 10
    def inc(self):
        self.count = self.count+1
        print(self.count)
    def list(self):
        self.t = 2
        for item in self.__dict__:
            print(repr(item))

t = Test()
v = '1'
ok = 'ok'
def mydebug(obj):
  print(repr(obj))

if __name__ == '__main__':
  #t.inc()
  #t.list()
  test.hello()