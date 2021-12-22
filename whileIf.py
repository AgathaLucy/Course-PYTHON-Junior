# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:57:37 2019

@author: 9
"""

#numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
#
#i=0
#max= len(numbers)-2

#while i<max:
#    print(numbers[i],numbers[i+1])
#    if numbers[i]**2==numbers[i+1]:
#        print('FOUND')
#    
#    i+=1

#while i<max:
#    print(numbers[i],numbers[i+1],numbers[i+2])
#    if numbers[i]**2==numbers[i+1] and numbers[i+1]**2==numbers[i+2]:
#        print('FOUND')
#    
#    i+=1
    
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i=0
max=len(texts)-1
while i<max:
    
    if len(texts[i])==len(texts[i+1]):
        print(texts[i],texts[i+1])
        print('FOUND')
    
    i+=1