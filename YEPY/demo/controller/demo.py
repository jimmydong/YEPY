# -*- coding: utf-8 -*-
"""
这是一个子模块的Demo
每一个Blueprint相当于一个controller
开发指导：
  1，修改或添加route规则（如果需要的话）
  2，开发处理逻辑（建议按照“add your code here”）
  3，修改config.py，将controller名字加入到blueprints列表中
"""
from flask import Blueprint, render_template, abort, request, current_app, make_response
from . import *
import bucket
import config
import os
### 以上为必备的模块，应用所需模块请在此下继续添加 ###
import time

controller = os.path.basename(__file__).split('.',1)[0]
blueprint = Blueprint(controller, __name__, url_prefix='/%s' % controller)

#action
@blueprint.route('/', defaults={'action':'index'}, methods=['GET','POST'])
@blueprint.route('/<action>/', methods=['GET','POST'])
def main(action):
    ############################################################################
    # init
    ############################################################################
    bucket._controller = controller
    bucket._action = action
    out = init()
    
    ############################################################################
    # add your code here
    ############################################################################
    out['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
    bucket.debug.time("action " + action + " begin")
    
    #处理action
    if action == 'index':
        do = request.args.get('do')
        debug = current_app.logger.debug
        log = bucket.debug.log
        if do == '1':
            #测试全局类
            g = bucket.G
            g.new = 'global - bucket.G'
            out.data = g.new
        elif do == '2':
            #测试缓存
            bucket.cache.set('haha','---kakaka, cache works OK!---')
            out.data = "Cache: %s" % bucket.cache.get('haha')
        elif do == '3':
            #使用Mysql
            from model import test
            n = test.Model()
            n.name = 't' + time.strftime("%H%M%S")
            n.value = 'From Demo' + time.strftime("%H%M%S")
            bucket.db.session.add(n)
            bucket.db.session.commit()
            t = test.Model.query.filter_by(id=1).first()
            out.data = "Mysql works OK -- %s" % t.name
        elif do == '4':
            #使用Mongo
            t = bucket.mongo.db.test.find({"name":"test"}).limit(1)
            out.data = 'Mongo: '
            for item in t:
                out.data = out.data + repr(item)
        else:
            out.data = "展开 firebug 查看 debug 信息 ， 点击右侧FDT查看 logger 信息"
            #使用logger
            current_app.logger.debug('test logger')
            #使用Debug
            bucket.debug.time("action " + action + " end")
            bucket.debug.log('debug:out', out)

    elif action == 'help':
        out['alert'] = request.args.get('alert')
        
    else: 
        #do something
        error = "未定义的action" 
    

    ############################################################################
    # finish
    ############################################################################
    return show(out)
