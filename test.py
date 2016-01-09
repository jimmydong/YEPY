# -*- coding: utf-8 -*-
"""
This is a temp test file
!这不是框架文件！
"""
import run

def hello():
  #想在这里调用统一的debug方法
  print(run.v)
  run.t.inc()
  run.mydebug("hello world" + run.ok)
  