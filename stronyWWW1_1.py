# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:38:31 2019

@author: 9
"""

import os
#przypisanie do zmiennej scieżki do pliku ze stronami internetowymi
filename = input('Please, enter the file path: ')
#pętla w razie błędnego wprowadzenia scieżki
while not os.path.isfile(filename):
    filename = input('Please, enter correct file path: ')

webAddresses=[]

file = open(filename,"r")
for site in file:
    webAddresses.append(site.replace('\n',''))
file.close()

dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')

filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')

for site in webAddresses:
    if site[-2:]=="pl":
        print("Adres '%s' jest adresem z Polski"%site)
        filePL.write(site+"\n")
    else:
        print("Adres '%s' nie jest adresem z Polski"%site)
        fileOther.write(site+"\n")

filePL.close()
fileOther.close()