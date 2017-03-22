#!/bin/sh
/usr/bin/nohup /usr/local/bin/python2.7 run_gevent.py >> log/access.log 2>&1 &
