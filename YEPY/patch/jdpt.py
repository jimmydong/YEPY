# -*- coding: utf-8 -*-
# JDPT (JimmyDong's Python Toolkits) 
# by jimmy.dong@gmail.com 2016.1.8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import time
import pprint
version = 0.1

def dump(obj):
  try:
    obj.__name__
  except:
    return repr(obj)
  try:
	  if '__dict__' in dir(obj):
	    newobj = obj.__dict__
	    if 'object at' in str(obj) and not newobj.has_key('__type__'):
	      newobj['__type__'] = str(obj)
	    for attr in newobj:
	      try:
	      	newobj[attr] = dump(newobj[attr])
	      except:
	        pass
	    return newobj
	  else:
			return obj
  except:
	  return 'NoneType'
def print_r(obj):
  try:
      raise Exception
  except:
      f = sys.exc_info()[2].tb_frame.f_back
      caller = "%s %s:%s" % (f.f_code.co_filename, f.f_code.co_name, f.f_lineno)
  print("###---------------------- jdpt:print_r  ---------------------------###")
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(dump(obj))
  print("[%s] from %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), caller))
  

def var_dump(obj, title=''):
  try:
      raise Exception
  except:
      f = sys.exc_info()[2].tb_frame.f_back
      caller = "%s %s:%s" % (f.f_code.co_filename, f.f_code.co_name, f.f_lineno)
  if title=='':
  	title = 'var_dump'
  print("###---------------------- jdpt:%s ---------------------------###" % title)
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(dump(obj))
  try:
    func = dir(obj)
  except:
    pass
  if len(func) > 0 :
    pp.pprint(func)
  print("[%s] from %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), caller))

__builtins__['print_r'] = print_r
__builtins__['var_dump'] = var_dump
print "patch jdpt/%s, hacked by jimmy.dong@gmail.com" % version