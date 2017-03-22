# YEPY - Yam Easy Python

Python项目快速开发原型

特点：

		1，Web接口，便于查看运行状况
		2，使用Flask，易于引入更多插件
		3，通过配置即可支持mongo/mysql/memcache/redis等
		4，controller/template模式
		5，使用bucket提供数据传递
		6，提供worker模式
		7，支持Firebug调试
		8，使用gevent支持大访问量

It's very small web framework for python. Current version is 1.0beta.

If you want join us, mailto://jimmy.dong@gmail.com

## Prepare:

	$ pip2.7 install ... [logging, flask, flask-debugtoolbar, flask-uploads, flask-cache, flask-pymongo, flask-sqlalchemy, python-memcached, pymongo, SQLAlchemy, yapf] 

推荐安装： ipython, notebook

	
## Usage:

copy demo/*  to your project folder as a new project

create directory dir: mkdir log

edit config.py, correct config yepf path

edit config.py, adopt other site parameters,

create your controller according to controller/demo.py, edit config.py to regist new controller

create your model and templates as your need

run:

	python application.py   --- windows 
	or
	$/bin/sh start.sh  --- linux
	
## Patch JDPT

copy patch/jdpt.py to %python_lib_path%/

add followings to %python_lib_path%/site.py

```
######################################################################
#  hack JDPT
import jdpt
######################################################################
```

Test
----

wait ...