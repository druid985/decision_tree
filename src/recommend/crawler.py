#coding=utf-8
from tools.tool import getPage
from BeautifulSoup import BeautifulSoup
'''
Created on 2015-12-15

@author: Administrator
'''

class crawler(object):
    '''
    classdocs
    '''


    def __init__(self,dbname):
        '''
        Constructor
        '''
        
    #为每个网页建立索引
    def addtoindex(self,url,soup):
        print 'Indexing %s' % url
        
    def crawl(self,urls,depth=2):
        for url in urls:
            html = getPage(url)
            if html is None or html == '' : continue
            
            soup = BeautifulSoup(html)
            url_list = []
            for link in soup('a'):
                url_str = link.get('href')
                if url_str is None or url_str == '' : continue
                elif url_str[0:4] == 'http' : url_list.append(url_str)
                else : pass
    
    def gettextonly(self,url,soap):
        

crawler = crawler('')     
print crawler.crawl(['http://zhidao.baidu.com/link?url=CCjcHNyvmsSjmFYWWSqBv4T_bL925XX2hPrRWhnUxyghg5rv-bprpTavkv18ge4U3OjzpIgEAytBv0sfG_rI7a'])