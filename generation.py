# -*- coding: UTF-8 -*-
"""
Created on Aug 24
input:
output:
@author: Lewis233
"""
from bs4 import BeautifulSoup
import constant
import file_oper

def get_stock_name(text):
    name_code = text.split(' ')[0]
    tmp = name_code.split('(')
    name = tmp[0].strip()
    code = tmp[1].strip(')')
    return [name, code]

def get_data(text):
    soup = BeautifulSoup(text, 'lxml')
    title = soup.find('title').string
    [name, code] = get_stock_name(title)

    table_bonus = soup.find_all(attrs={'class':'tableO'})[1]
    trs = table_bonus.find_all('tr')
    table = [];
    for i in range(1,len(trs)):
        if i%2 == 1:
            tmp = []
            #print(trs[i].find_all('td'))
            #print(trs[i].find_all('td')[1].string.strip())#除权除息日
            #print(trs[i].find_all('td')[2].string.strip())#派息信息
            try:
                #除权除息日
                tmp.append(trs[i].find_all('td')[1].string.strip())
            except:
                tmp.append(' ')
            try:
                #派息信息
                tmp.append(trs[i].find_all('td')[2].string.strip())
            except:
                tmp.append(' ')
        else:
            #print(trs[i].find_all('td')[1].string.strip())#分红年度
            #分红年度
            tmp.insert(0,trs[i].find_all('td')[1].string.strip())
            table.append(tmp)
    #print(table)#分红年度, 除权除息日, 派息信息
    return (name, code, table)



if __name__ == '__main__':
    root = constant.root
    f = open(root+'/600028.html','r',encoding = 'utf-8')
    text = f.read()
    result = get_data(text)
    print(result[0])
    print(result[1])
    file_oper.write(result[2],root+'/'+result[0]+'.csv')
