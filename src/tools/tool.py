import json  
import urllib2
'''
Created on 2015-12-9

@author: Administrator
'''

def print_new(object):
    if type(object) == list or dict :
        print json.dumps(object, encoding="UTF-8", ensure_ascii=False)
    else:
        print object

def getPage(url,resource,parameter):
    try:
        c = urllib2.urlopen(url)
    except:
        return None
    return c.read()