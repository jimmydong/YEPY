#!/bin/sh
/usr/bin/nohup /usr/local/bin/python2.7 application.py >> log/access.log 2>&1 &
