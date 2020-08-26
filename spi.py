# -*- coding: UTF-8 -*-
"""
Created on Aug 23
input:
output:
@author: Lewis233
"""

import requests
from bs4 import BeautifulSoup
import constant

def crawl(url,file_name):
    headers = {'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'}
    strhtml = requests.get(url,headers=headers)
    f = open(constant.root+'/'+file_name+'.html','w', encoding = 'utf-8')
    f.write(strhtml.text.strip())
    f.close()

if __name__ == "__main__":
    crawl('https://q.stock.sohu.com/cn/600028/fhsp.shtml','600028')
