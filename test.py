# -*- coding: UTF-8 -*-
"""
Created on Aug 25
input:
output:
@author: Lewis233
"""
import spi
import file_oper
import constant
import generation
import sys

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import math

def func(x, a, b):
    return a * np.exp(b * x)

code = sys.argv[1]
spi.crawl('https://q.stock.sohu.com/cn/'+code+'/fhsp.shtml',code)

root = constant.root

f = open(root+'/'+code+'.html','r',encoding = 'utf-8')
text = f.read()
result = generation.get_data(text)
print(result[0])
print(result[1])
file_oper.write(result[2],root+'/'+result[0]+'.csv')
bonus = [];
year = [];
for i in result[2]:
    strfloat = i[2].split('每10股派息')[-1].split('元')[0]
    bonus.append(float(strfloat))
    year.append(i[0].split('-')[0])
print(bonus)
print(year)
year_num = year[4::-1]#list(map(int, year[4::-1]))
xdata =  np.linspace(1,5,5)
ydata = bonus[4::-1]
plt.plot(year_num,ydata,'b-')
popt, pcov = curve_fit(func, xdata, ydata)
#popt数组中，三个值分别是待求参数a,b,c
y2 = [func(i, popt[0],popt[1]) for i in xdata]
plt.plot(year_num,y2,'r--')

rate = math.exp(popt[1])-1
print(rate)
print(bonus[0]/(0.07-rate))

plt.show()
