# -*- coding: utf-8 -*-
"""
default模块
by jimmy.dong@gmail.com 2016.1.4

注意：开发controller请以demo为参照
"""
from flask import Blueprint, render_template, abort, request, current_app, make_response
from . import *
import bucket

controller = 'index'
blueprint = Blueprint(controller, __name__)

#action
@blueprint.route("/favicon.ico")
def favicon():
    return make_response("")

@blueprint.route("/", defaults={'action':'index'}, methods=['GET','POST'])
@blueprint.route('/<action>', methods=['GET','POST'])
def main(action):
    #init
    bucket._controller = controller
    bucket._action = action
    out = init()  # @UndefinedVariable
    
    #add your code here
    out.info = "<pre> ----==== YEPY Demo by jimmy.dong@gmail.com ====---- \n 开始运行于： %s \n 累积执行： %d  \n 运行成功： %d </pre>" % (bucket.G.begin_time, bucket.G.counter, bucket.G.counter_success)
    out.data = " ----==== current_app.config ====----  \n"
    if action == 'index':
        for k in current_app.config:
            out.data = out.data + " %s  -   %s \n" % (k,current_app.config[k])
        pass
    else: 
        out.data = " --- error Can't find the action."
        pass 
        
    #finish
    return show(out)  # @UndefinedVariable
