# -*- coding: utf-8 -*-
"""
YEPY 控制器模块
by jimmy.dong@gmail.com

增加控制器的步骤：
1，新建xxxx.py
2，修改config.py[核心配置]，注册新控制器
"""
from flask import Blueprint, render_template, abort, request, current_app, make_response
from jinja2 import TemplateNotFound
import bucket
_yepy_controller_version = '1.0b'

def init():
    # init before action
    out = bucket.ConfigG()
    return out

def show(out):
    # show after action
    try:
        if bucket._controller == 'index':
            response = make_response(render_template('%s.html' % (bucket._action), out=out))
        else:
            response = make_response(render_template('%s/%s.html' % (bucket._controller,bucket._action), out=out))
        return response
    except TemplateNotFound:
        abort(404)
