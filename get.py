# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:42:01 2020

@author: 11575
"""
import requests
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
print(strhtml.text)
