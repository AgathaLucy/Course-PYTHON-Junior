# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:18:14 2019

@author: 9
"""
#Zad 1
import random
#Zad2
#for i in range(1,11):
#    numb = random.randint(1,100)
#    print(i,numb)
#Zad3
#number1=random.randint(1,100)
#counter=trials=0
#number0=random.randint(1,100)
#print('Chosen number: %d'%number1)
#while number0!=number1:
#    number0=random.randint(1,100)
#    trials+=1
#    counter=trials
#    print('Number: %3d, trial: %5d.'%(number0,counter))
#print('Trials number %d'%(trials))
#Zad4
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)
groupNumber=0
for country in countries:
    if countries.index(country)%4==0:
        groupNumber+=1
        print("----Grupa %d----"%groupNumber)
    print(country)
