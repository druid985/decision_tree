#coding=utf-8
import json  
import urllib2
import MySQLdb
'''
Created on 2015-12-9

@author: Administrator
'''

def print_new(object):
    if type(object) == list or dict :
        print json.dumps(object, encoding="UTF-8", ensure_ascii=False)
    else:
        print object

def getPage(url):
    try:
        c = urllib2.urlopen(url)
    except:
        print '%s 读取失败' % url
        return None
    return c.read()

#try:
#    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test',port=3306)
#    cur=conn.cursor()
#    count = cur.execute('select * from link')
#    print 'there has %s rows record' % count
#    results=cur.fetchall()
#    for r in results:
#        print r[1]
#    
#    cur.close()
#    conn.close()
#except MySQLdb.Error,e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])