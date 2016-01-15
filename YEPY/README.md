# YEPY - Yep! Easy Python

It's very small web framework for python. Current version is 0.01beta.

If you want join us, mailto://jimmy.dong@gmail.com

## Prepare:

	$ pip2.7 install ... [logging, flask, flask-debugtoolbar, flask-uploads, flask-cache, flask-sqlalchemy, python-memcached, pymongo, SQLAlchemy, yapf] 

推荐安装： ipython, notebook

	
## Usage:

copy demo/*  to your project folder as a new project

edit config.py to config site parameters,

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

wait...