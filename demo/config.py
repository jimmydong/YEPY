# -*- coding: utf-8 -*-
""" 
YEPY 核心配置文件
提示：
    请先阅读YEPY/README.md
    请将demo复制到新目录再开始开发
    hack lib/site.py with jdpt, so you can use: print_r/var_dump 
"""
from flask import Flask
from werkzeug.utils import import_string
import logging
from logging.handlers import RotatingFileHandler
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os

_yepy_application_version = '1.0b'
_yepy_path = '../'
sys.path.append(_yepy_path) #如果yepy不在当前目录

online = ['web01','web02','db01','db02','rd01']
if os.getenv('HOSTNAME') in online:
    product = True
else:
    product = False

#Flask配置
class Config(object):
    APP_HOST = '0.0.0.0'
    APP_PORT = 8888
    DEBUG = False
    USE_RELOADER = False # 禁止代码自动更新，防止运行多次
    TESTING = False
    SECRET_KEY = "01234567890@2015"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SESSION_COOKIE_NAME = "YEPY_SESSION"
    
    CACHE_ENABLE = True
    CACHE_KEY_PREFIX = "YEPY_" 
    CACHE_MEMCACHED_SERVERS = ["127.0.0.1:11211"]
    CACHE_REDIS_HOST = "123.57.173.188"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_PASSWORD = "yishengDaojia@2015ASDFGHJKL12345"
    
    SQLALCHEMY_DATABASE_URI = "mysql://localhost:3306/test"
    SQLALCHEMY_BINDS = {
                        'master':   'mysql://localhost:3306/test',
                        'slave':    'mysql://localhost:3306/test'
                        }
    #TABLE_PREFIX = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    MONGO_URI = "mongodb://yisheng:yisheng%402015@211.152.8.45:27017/yisheng"
    MONGO_SOCKET_TIMEOUT_MS = "3000"
    MONGO_CONNECT_TIMEOUT_MS = "3000"
    
    UPLOADS_DEFAULT_DEST = "static/upload"
    UPLOADS_DEFAULT_URL = "/upload"
    #UPLOADED_FILES_ALLOW = []
    #UPLOADED_FILES_DENY = []
    
    LOG_FILE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    USE_RELOADER = True

    DEBUG_TB_PROFILER_ENABLED = True  #注意：极大影响性能
    LOG_FILE = 'log/logger.txt'
    LOG_SIZE = 10000
    
class ProductionConfig(Config):
    DEBUG_TB_PROFILER_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:sfKpN3KEhVXrm6XU@db02:8307/test"
    SQLALCHEMY_BINDS = {
                        'master':   'mysql://root:sfKpN3KEhVXrm6XU@db02:8307/test',
                        'slave':    'mysql://root:sfKpN3KEhVXrm6XU@db02:8307/test'
                        }
    
# 应用模块
blueprints = [
              'controller.default:blueprint',
              'controller.demo:blueprint'
              ]
def createApp():
    app = Flask(__name__)
    #注册模块
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)
    #根据情况加载测试或正式配置
    if product == True: 
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    if app.config['LOG_FILE']:
        file_handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=app.config['LOG_SIZE'], backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)
    return app
