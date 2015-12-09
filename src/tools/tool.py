import json  
'''
Created on 2015-12-9

@author: Administrator
'''

def print_new(object):
    if type(object) == list or dict :
        print json.dumps(object, encoding="UTF-8", ensure_ascii=False)
    else:
        print object
        
    
