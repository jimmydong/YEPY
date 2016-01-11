# -*- coding: utf-8 -*-
"""
default模块
by jimmy.dong@gmail.com 2016.1.4

注意：开发controller请以demo为参照
"""
from flask import Blueprint, render_template, abort, request, current_app, make_response
from jinja2 import TemplateNotFound
from . import *
import bucket

controller = 'index'
blueprint = Blueprint(controller, __name__)

#action
@blueprint.route("/favicon.ico")
def favicon():
  return make_response("")

@blueprint.route("/", defaults={'action':'index'}, methods=['GET','POST'])
@blueprint.route('/<action>/', methods=['GET','POST'])
def main(action):
    #init
    bucket._controller = controller
    bucket._action = action
    out = init()  # @UndefinedVariable
    
    #add your code here
    if action == 'index':
        #do something
        pass
    else: 
        #do something
        pass 
        
    #finish
    return show(out)  # @UndefinedVariable
