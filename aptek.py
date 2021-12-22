# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 01:06:22 2019

@author: 9
"""

import os
import datetime

dataInputCatalog = r'C:\Users\9\Desktop\Pulpit\cwiczeniaZPythona\dataInput'
dataOutputCatalog = r'C:\Users\9\Desktop\Pulpit\cwiczeniaZPythona\dataOutput'

today = datetime.date.today()
todayOutputCatalog = os.path.join(dataOutputCatalog, today.strftime("%Y-%m-%d"))

isInputCatalogOk = os.path.isdir(dataInputCatalog)
isOutputCatalogOk = os.path.isdir(dataOutputCatalog)
isTodayOutputCatalogOk = not(os.path.isdir(todayOutputCatalog)) and \
                         not(os.path.isfile(todayOutputCatalog))



if isInputCatalogOk and isOutputCatalogOk and isTodayOutputCatalogOk:
    print('Conditions met! We can continue!')
else:
    print('Prerequisits not met! Check the paths!')
if not isInputCatalogOk:
    print('The input directory is missing!')
if not isOutputCatalogOk:
    print('The output directory is missing!')
if not isTodayOutputCatalogOk:
    print('Today\'s output directory already exists!')
    