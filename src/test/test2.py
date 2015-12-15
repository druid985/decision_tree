import urllib2
from BeautifulSoup import BeautifulSoup
from tools.tool import getPage
'''
Created on 2015-12-14

@author: Administrator
'''
 
url = 'http://vacations.ctrip.com/grouptravel/p3900836s2.html#ctm_ref=ssc_hp_tour_bst_pro_01'
html = getPage(url)
soup = BeautifulSoup(html)
#best_an = soup('pre')[0]
file = open('b.txt','w+') 
file.write(soup.prettify())
#soup2 = BeautifulSoup(str(best_an))
#file = open('c.txt','w+') 
#file.write(soup2.prettify())