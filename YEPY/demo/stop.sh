#!/bin/sh
kill `cat application.pid`
rm application.pid -f