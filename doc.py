# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:38:22 2019

@author: 9
"""
musclePain = False
fever = True
weakness = True
isMan = True

if musclePain and fever and weakness:
    print('Suspiction of influenza')
else:
    print('The flu is unlikely')

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('Suspiction of influenza')
elif weakness and not fever:
    print('Just take a rest!')
else:
    print('You may be cold')

isCheckCompleted = True
print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET!')