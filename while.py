# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:49:10 2019

@author: 9
"""

firstRow = 1
lastRow = 31
currentRow = firstRow
while currentRow <= lastRow:
    print('Row number',currentRow)
    currentRow += 1
print('------------------------------')
start = 1
end = 14
i = start
while i !=end:
    print(i,'podniesone do kwadratu wynosi:',str(i**2),', a podniesione do szecianu wynosi:',str(i**3)+'.')
    i+=1
print('------------------------------')
poczatek = 0
koniec = 16
x=poczatek
while x<=koniec:
    print(2**x)
    x+=1
print('------------------------------')

z=1
while z<=10:
    print(z*'x')
    z+=1