# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:09:43 2019

@author: 9
"""

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
#for error in data:
#    print(error.upper())
elements = []
#
#for error in data:
#    elements = error.split(":")
#    print(elements[0].upper(),elements[1])

for error in data:
    elements = error.split(":")
    if elements[0] == "Error":
        print(elements[0],elements[1].upper())
    else:
        print(elements[0],elements[1])