# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:11:09 2019

@author: 9
"""
MIN_LIKES = 500
MIN_SHARES = 100
num_likes = 1300
num_shares = 5
price = 100

if num_likes>=MIN_LIKES and num_shares>=MIN_SHARES:
    price = price*0.9
    print('Ubrania kosztują teraz o 10 % mniej.')
elif num_likes<500:
    print('Za mało polubień.')
elif num_shares<100:
    print('Za mało udostępnień.')

    

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Otrzymujesz kupon na Burgera')
elif isWeekend:
    print('Promocja obowiązuje w dni robocze od pon. do pt.')
elif not (isPizzaOrdered or isBigDrinkOrdered):
    print('Nie zamówiłes żadnego produktu.')
else:
    print('Trzeba zamówić cole lub pizze.')
    
diskSize = 150
diskSizeUsed = 133
fileSize = 10
if fileSize <= (diskSize - diskSizeUsed):
    print('File can be downloaded')
else:
    print('Za mało miejsca na dysku')
