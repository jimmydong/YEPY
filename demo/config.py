# -*- coding: utf-8 -*-
""" 
YEPY 核心配置文件
"""
from flask import Flask
from werkzeug.utils import import_string
import logging
from logging.handlers import RotatingFileHandler
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os

_yepy_application_version = '1.0b'
_yepy_path = '../'
sys.path.append(_yepy_path) #如果yepy不在当前目录

#正式服务器配置，自动识别测试环境
online = ['web01','web02','db01','db02','rd01']
if os.getenv('HOSTNAME') in online:
    product = True
else:
    product = False

#Flask配置
class Config(object):
    APP_NAME = 'YEPY-Demo'
    APP_HOST = '0.0.0.0'
    APP_PORT = 9999
    DEBUG = False
    TESTING = False
    SECRET_KEY = "01234567890@2015"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SESSION_COOKIE_NAME = "YEPY_SESSION"
    
    CACHE_ENABLE = False
    CACHE_KEY_PREFIX = "YEPY_" 
    CACHE_MEMCACHED_SERVERS = ["127.0.0.1:11211"]
        
    UPLOADS_DEFAULT_DEST = "static/upload"
    UPLOADS_DEFAULT_URL = "/upload"
    #UPLOADED_FILES_ALLOW = []
    #UPLOADED_FILES_DENY = []
    
    LOG_FILE = 'log/logger.txt'
    LOG_SIZE = 10000
    
class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True  #注意：极大影响性能
    
class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_PROFILER_ENABLED = False
    
    
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
