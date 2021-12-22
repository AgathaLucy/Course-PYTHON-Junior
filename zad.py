# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:59:26 2019

@author: 9
"""
#startNumber = 0
#endNumber = 50
#i = startNumber
#suma = 0
#
#while i<endNumber:
#    suma = 2*i+1
#    print(str(i),"+",str(i+1),"=",str(suma))
#    i+=1

number = 1
previouNumber=0

while number<=50:
    print(number+previouNumber)
    previouNumber = number
    number+=1
    
#import random
#
#myNumber=random.randint(0,20)
#guess = -1
#trial = 0
#print('Guess my number')
#while guess != myNumber:
#    guess = int(input('>>'))
#    if guess==myNumber:
#        print('Congratulation!!')
#    elif guess > myNumber:
#        print('My number is smaller than your guess. Try again.')
#    else:
#        print('My number is greater than your guess. Try again.')
#    trial+=1
#    
#print('Trials number:',str(trial))