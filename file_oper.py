# -*- coding: UTF-8 -*-
"""
Created on Aug 24
input:
output:
@author: Lewis233
"""

def write(data_list, file_path):
    f = open(file_path,'w', encoding = 'gbk')
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            f.write(data_list[i][j].strip())
            if j != len(data_list[i])-1:
                f.write(',')
            else:
                f.write('\r')
    f.close()

def read(file_path):
    f = open(file_path,'r',encoding = 'gbk')
    str_csv = f.read().strip()#.decode('gbk').encode('utf-8')
    f.close()

    result = []
    tmp = []
    for item in str_csv.split('\n'):
        tmp = item.split(',')
        result.append(tmp)
    return result
