# -*- coding: utf-8 -*-
""" 
DEMO: 完成工作任务的子线程
by jimmy.dong@gmail.com 2015.01.14
"""
import bucket # 加载全局变量
import time
def job():
    if not bucket.G.job_begin:
        bucket.G.job_begin = True
    else:
        return False
    for i in range(0,10):
        print("--------- job running... %d ---------- \n"  % i)
        bucket.G.counter = i
        time.sleep(1)
