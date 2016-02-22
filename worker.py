# -*- coding: utf-8 -*-
""" 
工作线程（后台工作部分）
"""
import bucket  # 加载全局变量
import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,
                                                     ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble, 
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class WorkerThread(threading.Thread):
    def _get_my_tid(self):
        """determines this (self's) thread id"""
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")
        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id
        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid
        raise AssertionError("could not determine the thread's id")
    
    def raiseExc(self, exctype):
        """raises the given exception type in the context of this thread"""
        _async_raise(self._get_my_tid(), exctype)


    def terminate(self):
        """raises SystemExit in the context of the given thread, which should 
        cause the thread to exit silently (unless caught)"""
        self.raiseExc(SystemExit)

class Worker():
    thread = None
    status = False
    
    def setJob(self, job):
        print_r(self.thread)
        if self.thread and self.thread.isAlive():
            #已经有进程在运行
            return False
        self.thread = WorkerThread(target=job)
        self.status = 'init'
        return self.thread
    
    def checkStatus(self):
        if not self.thread:
            self.status = False
        if self.thread and self.status == 'init' and self.thread.isAlive():
            self.status = 'running'
        elif self.thread and self.status == 'running' and not self.thread.isAlive():
            self.status = 'finish'
        return self.status