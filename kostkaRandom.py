# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:53:36 2019

@author: 9
"""

import random
min=1
max=6
dice=random.randint(1,6)

if dice==1:
    print('''
      
 o 
   
 ''')
elif dice==2:
    print('''
  o
   
o  
 ''') 
elif dice==3:
    print('''
  o
 o 
o  
 ''') 
 
elif dice==4:
    print('''
o o
   
o o
 ''')
 
elif dice==5:
    print('''
o o
 o 
o o
''') 
elif dice==6:
     print('''
o o
o o
o o
''')
print('------------------------------------------')    


dice=[]

for i in range(5):
    throw=random.randint(1,6)
    

    if throw==1:
        result='''
   
 o 
   
 '''
    elif throw==2:
         result='''
  o
   
o  
 '''
    elif throw==3:
         result='''
  o
 o 
o  
 '''
 
    elif throw==4:
        result='''
o o
   
o o
 '''
 
    elif throw==5:
         result='''
o o
 o 
o o
'''

    elif throw==6:
        result='''
o o
o o
o o
'''
    dice.append(result)

dice.sort()   
print(dice[])