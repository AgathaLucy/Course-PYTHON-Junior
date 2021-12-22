# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:10:23 2019

@author: 9
"""

import os

#deklaracja listy stron internetowych
webAddresses=[]

#wprowadznie przez użytkownika witryn 
line = input('Please, enter website address: ')
while line != '' :
    webAddresses.append(line)
    line = input('Please, enter another website address,\n(if you don\'t want press ENTER): ')

#przypisanie scieżki bieżącego katalogu do zmiennej
dirName = os.getcwd()

#zadeklarowanie zmiennej, przechowującej nazwę pliku podaną przez użytkownika
fileName=input('Please, enter file name with it\'s extension: ')

#łączenie bieżącej cieżki i nazwy pliku
filePath=os.path.join(dirName,fileName)

#I sposób na otwarcie pliku i zapisanie do niego adresów
with open(filePath,'a+') as webSites:
    for site in webAddresses:
        webSites.write(site+'\n')

#II sposób na otwarcie pliku i zapisanie do niego adresów
webSites = open(filePath,'a+')
for site in webAddresses:
    webSites.write(site+'\n')
webSites.close()