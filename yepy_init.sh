#!/bin/sh

#scp -r db02:/root/Python-2.7.10 .
#cd Python-2.7.10
#./configure
#make && make install
#cd ..
#rm -Rf Python-2.7.10*

yum install mysql-community-client mysql-community-libs
yum install mysql-devel
yum install MySQL-python

scp db02:/root/MySQL-python-1.2.3.tar.gz .
tar -xzvf MySQL-python-1.2.3.tar.gz
cd MySQL-python-1.2.3
python2.7 setup.py install
cd ..
rm MySQL-python-1.2.3* -Rf

wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py -O - | python2.7
wget --no-check-certificate "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz"
tar -xzvf pip-1.5.4.tar.gz
cd pip-1.5.4/
python2.7 setup.py
python2.7 setup.py install
cd ..
rm pip-1.5.4* -Rf

pip2.7 install logging
pip2.7 install flask
pip2.7 install flask-debugtoolbar
pip2.7 install flask-uploads
pip2.7 install flask-cache
pip2.7 install flask-pymongo
pip2.7 install flask-sqlalchemy
pip2.7 install python-memcached
pip2.7 install pymongo
pip2.7 install SQLAlchemy
pip2.7 install MySQL-python
pip2.7 install setproctitle
pip2.7 install yapf


#cp /WORK/PYTHON/YEPY/patch/jdpt.py /usr/lib64/python2.7/
#echo "#Hack JDPT" >> /usr/lib64/python2.7/site.py
#echo "import jdpt" >> /usr/lib64/python2.7/site.py

#windows下组件包： http://www.lfd.uci.edu/~gohlke/pythonlibs/
