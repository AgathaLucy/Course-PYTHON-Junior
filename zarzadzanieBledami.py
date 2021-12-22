# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:46:05 2019

@author: 9
"""
import sys

file_path = r'C:\Users\9\Desktop\Pulpit\cwiczeniaZPythona\dataInput\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])            
            print('Order from drugstore "%s", item "%s", amount %d.'%(pharmacy_name, item, amount))
        
        except ValueError as o:
            print('Error: "',o,'" Error is in line %s'%line)
        
        except IndexError as e:
            print('Error: "',e,'" Error is in line %s'%line)
        
        except:
            print('The error occurred in the line %s.'%line)
            print(sys.exc_info()[0])
            
print("Processing finished")