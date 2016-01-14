# -*- coding: utf-8 -*-
""" 
DEMO : How to use YEPY
by jimmy.dong@gmail.com 2015.12.31

Use::
  python application.py
  Then navigate your browser to: ``http://localhost:8888``
"""
import config # 加载配置文件
import bucket # 加载全局变量
from flask import Flask, render_template, request, make_response
from flask_debugtoolbar import DebugToolbarExtension
from flask_uploads import configure_uploads, UploadSet
from worker import WorkerThread
import cgi
import os
import time

#The Flask Application
app = config.createApp()
if app.config['DEBUG']:
    bucket.debug.start()  # @UndefinedVariable

#初始化核心插件
if app.config['CACHE_ENABLE']:
    bucket.cache.init_app(app, config={'CACHE_TYPE':'memcached'}) # 'simple' | 'memcached' | 'redis'
if app.config['SQLALCHEMY_DATABASE_URI']:
    bucket.db.init_app(app)
if app.config['MONGO_URI']:
    bucket.mongo.init_app(app)
toolbar = DebugToolbarExtension(app)
photos = UploadSet(name='photos',extensions=('jpg','gif','png'))
files = UploadSet(name='files',extensions=('txt','rar','zip')) 
configure_uploads(app,(photos,files))

# Framework
@app.before_request
def before_request():
    bucket.debug.reload()  # @UndefinedVariable
    pass
@app.after_request
def after_request(response):
    if request.url_root.find('/static/') > -1:
        return response
    bucket.debug.time('after')
    headers = bucket.debug.show()  # @UndefinedVariable
    if len(headers) > 0:
        for key in headers:
            response.headers[key] = headers[key]
    response.headers["Server"] = "Python/Power by YEPY %s" % config._yepy_application_version
    response.headers["Expires"] = "Expires: Mon, 26 Jul 1997 05:00:00 GMT"
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Pragma"] = "no-cache"
    return response
#@app.teardown_request
#def teardown_request():
#    pass
with app.app_context():
    pass

#上传处理
@app.route("/uploadPhoto", methods=['GET','POST'])
def uploadPhoto():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return photos.url(filename)
    else:
        return "No photo uploaded!"

#异常处理
@app.errorhandler(404)
def not_found(error):
    out = repr(app.url_map)
    response = make_response('页面未找到 page not found <br/><pre>' + cgi.escape(out) + '</pre>', 404)
    return response

@app.route("/test")
def test():
    return "Hello World!"

bucket.G.counter = 0
def job():
    for i in range(0,10):
        print_r(i)
        bucket.G.counter = i
        time.sleep(1)


if __name__ == '__main__':
    #设置PID
    pid = os.getpid()
    pidfile = file("application.pid","w")
    pidfile.write(str(pid))
    pidfile.close()
    
    #启动工作线程
    worker = WorkerThread(target=job)
    worker.setDaemon(True)
    worker.start()
    
    #启动监听
    app.run(host=app.config['APP_HOST'],port=app.config['APP_PORT'])
    
    #程序结束
    if worker.isAlive():
        print("warnning: worker尚未完成，提前终止")
    #os.remove("application.pid")
    print(" ---=== application finished! ===---")