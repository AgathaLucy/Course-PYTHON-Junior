# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:12:56 2019

@author: 9
"""

import os
import sys


line = input('For how much would you have bought another Udemy course?:')

filePath = input('Enter the file path:')

try:
    with open(filePath,'w') as file:
        file.write(line)
    value = int(line)
    print('The value saves in file is:',value)

except FileNotFoundError as o:
    print('\nError opening file:',filePath,o)

except ValueError as o:
    print('The value entered cannot be converted to a number.',line,o)

except:
    print('SORRY - WE HAVE AN ERROR. PLEASE TRY AGAIN.', sys.exc_info()[0] )
else:
    print('Actions completed successfully.')