# -*- coding: utf-8 -*-
"""
YEPF 数据对象模型

-- 表的结构 `test`
CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
ALTER TABLE `test` ADD PRIMARY KEY (`id`);
ALTER TABLE `test` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT
"""
from flask import current_app, request, url_for
from bucket import db 
import os

tablename = os.path.basename(__file__).split('.',1)[0]
class Model(db.Model):
    __tablename__ = tablename
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    value = db.Column(db.String(200))
    
    @staticmethod
    def getNameById(id):
        row = Test.query.filter_by(id=id).first()
        if row is None:
            return False
        else:
            return row.name
    
        