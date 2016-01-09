# -*- coding: utf-8 -*-
"""
YEPY 调试模块
by jimmy.dong@gmail.com 2016.1.4

建议安装firephp查看
"""
import numbers
import json
import inspect
import collections

class FirePhp:
    #配置
    _option = {"maxDepth":5,"maxArrayDepth":5, "maxObjectDepth":5, "maxLength":1024}
    _version = 0.3
    
    def __init__(self):
        self.reload()
    
    def reload(self):
        self.messageIndex = 1
        self.headers = collections.OrderedDict()        
        
    def fb(self, object, title='Other Debug Info', skip=1):
        if len(object)<skip+1:
            return False
        
        self.setHeader('X-Wf-Protocol-1','http://meta.wildfirehq.org/Protocol/JsonStream/0.2')
        self.setHeader('X-Wf-1-Plugin-1','http://meta.firephp.org/Wildfire/Plugin/FirePHP/Library-FirePHPCore/%s' % self._version)
        self.setHeader('X-Wf-1-Structure-1','http://meta.firephp.org/Wildfire/Structure/FirePHP/FirebugConsole/0.1')
        
        structure_index = 1
        msg_meta = collections.OrderedDict()
        msg_meta["Type"] = "TABLE"
        msg_meta["FILE"] =""
        msg_meta["Line"] =""
        msg = "[%s,[\"%s\",%s]]"  % (self.jsonEncode(msg_meta),title,self.jsonEncode(object))
        if len(msg) < 5000:
            self.setHeader("X-Wf-1-%d-1-%d" % (structure_index,self.messageIndex), "%d|%s|" % (len(msg),msg) )
            self.messageIndex = self.messageIndex + 1
        else:
            trunk = self.chunkSplit(msg, 5000)
            for flag,part in trunk:
                if flag == 'begin':
                    setHeader('X-Wf-1-' + structure_index + '-1-' + self.messageIndex, len(msg) + '|' + part + '|\\')
                elif flag == 'end':
                    setHeader('X-Wf-1-' + structure_index + '-1-' + self.messageIndex, '|' + part + '|')
                else:
                    setHeader('X-Wf-1-' + structure_index + '-1-' + self.messageIndex, '|' + part + '|\\')
                self.messageIndex = self.messageIndex + 1
        self.setHeader('X-Wf-1-Index',self.messageIndex-1)
        return True
    
    def setHeader(self, name, value):
        self.headers[name] = value
        return True
        
    def chunkSplit(self, str, length = 1000, end = "\n"):
        strlen = len(str)
        n = int( (strlen-1) / length ) + 1
        for i in range(n):
            flag = ''
            start = i * length
            end = (i+1) * length
            if end >= ( strlen):
                end = strlen
                flag = 'end'
            if i == 0:
                flag = 'begin'
            yield flag, str[start:end]
        
    def jsonEncode(self, object, skipObjectEncode = False):
        if not skipObjectEncode:
            object = self.encodeObject(object)
        return json.dumps(object)
    
    def encodeTable(self, table):
        if not table:
            return table
        
        new_table = []
        for row in table:
            if isinstance(row, list):
                new_row = []
                for item in row:
                    new_row.append(self.encodeObject(item))
                new_table.append(new_row)
        return new_table

    def encodeObject(self, object, objectDepth = 1, arrayDepth = 1, maxDepth = 1):
        if maxDepth > self._option['maxDepth']:
            return '** Max Depth (' + self._option['maxDepth'] + ') **'
        
        if isinstance(object, basestring):
            if len(object) > self._option['maxLength']:
                 return Object[:self._option['maxLength']]
            else:
                return object
        elif isinstance(object, numbers.Number):
            return object.__repr__()
        elif isinstance(object, tuple):
            return object.__repr__()
        elif isinstance(object, list):
            if arrayDepth > self._option['maxArrayDepth']:
                return '** Max Array Depth (' + self._option['maxArrayDepth'] + ') **'
            else:
                result = []
                for item in object:
                    result.append(self.encodeObject(item, objectDepth, arrayDepth+1, maxDepth+1))
                return result
        elif(isinstance(object, collections.OrderedDict)):
            if arrayDepth > self._option['maxArrayDepth']:
                return '** Max Array Depth (' + self._option['maxArrayDepth'] + ') **'
            else:
                result = collections.OrderedDict()
                for key in object:
                    result[key] = self.encodeObject(object[key], objectDepth, arrayDepth+1, maxDepth+1)
                return result
        elif isinstance(object, dict):
            if arrayDepth > self._option['maxArrayDepth']:
                return '** Max Array Depth (' + self._option['maxArrayDepth'] + ') **'
            else:
                result = collections.OrderedDict()
                for key in object:
                    result[key] = self.encodeObject(object[key], objectDepth, arrayDepth+1, maxDepth+1)
                return result
        elif inspect.isbuiltin(object):
            return object.__repr__()
        else:
            if objectDepth > self._option['maxObjectDepth']:
                return '** Max Object Depth (' + self._option['maxObjectDepth'] + ') **'
            try:
                result = collections.OrderedDict()
                t =  str(object.__class__)
                result['object'] = t.split('at')[0]
                for key in vars(object):
                    if key[:2] == '__':
                        pass
                    else:
                        result['public:' + key] = self.encodeObject(getattr(object,key), objectDepth+1, arrayDepth, maxDepth+1)
                return result
            except TypeError:
                print 'error',
                return object.__repr__()

if __name__ == '__main__':
    f = FirePhp()
    f.test1 = 'hello'
    f.test2 = 'world'
    #t = f.jsonEncode(f)
    #for t in f.chunkSplit("abcdeabcdeabcdeabcdeabcdeabcde1", 5):
    #    print t
    f.fb([["A","B","C"],["1","2","3"],["4","5","6"]])
    print(repr(f.header))