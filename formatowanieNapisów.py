# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:10:37 2019

@author: 9
"""

helloMessage = 'Hello %s!'
print(helloMessage%'Chirs')
print(helloMessage%'Kate')
print('\n')
helloMessage1 = 'Hello {0:s}!'
print(helloMessage1.format('Chirs'))
print(helloMessage1.format('Kate'))
print('\n')
helloMessage2 = '%s has %d %s'
print(helloMessage2%('Chirs',1,'animal'))
print(helloMessage2%('Kate',100000,'$'))
print('\n')
helloMessage3 = '{0:s} has {1:d} {2:s}'
print(helloMessage3.format('Chirs',1,'animal'))
print(helloMessage3.format('Kate',100000,'$'))
print('\n')

print('%20s costs %6d €'%('ICE CREAM',3))
print('%20s costs %6d €'%('TRIP TO VENICE',119))
print('%20s costs %6d €'%('PIZZA HAWAI',6))

line = "{0:20s} costs {1:6d} €"
 
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))