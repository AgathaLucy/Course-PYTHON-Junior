# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:10:27 2019

@author: 9
"""
filePath = r'C:\Users\9\Desktop\Pulpit\cwiczeniaZPythona\dataInput\orders.csv'

with open(filePath,"r") as file:
    
    for line in file:
    
        #line = line[:-2]
        line = line.replace('\n','')
        order=line.split(',')
        
        if len(order)==3:
            print('Order from drugstore "%s", item "%s", amount %s.' %(order[0],order[1],order[2]))
        else:
            print('Line "%s" malformed!!!' %line)
            
print("Processing finished")