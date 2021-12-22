# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:50:59 2019

@author: 9
"""
#Program, którym ćwiczę funkcje wejcia-wyjcia. Spradzam czy istnieja
#foldery, pliki oraz sprawdzam ich właciwosci.


import os
import time

dir = input("Enter the path to the directory: ")
# Poniższa funckja sprawdza czy dana cieżka prowadzi do katalogu/folderu
if not os.path.isdir(dir):
    print('%s do not exist.'%dir)
else:
    file = input("Enter the name of the file: ")
    path = os.path.join(dir,file)
    #Poniższa funkcja sprawdza czy istnieje element o danej scieżce
    if os.path.exists(path):
        #Złożenie funkcji zwraca nam datę ostatniej modyfikacji, wskazuje
        #na to literka m w os.path.get"m"time(path), oprócz niej można wpisać
        #c - oznacza datę utworzenia lub a - oznacza czas ostaniej modyfikacji.
        print('Last modyfication',time.localtime(os.path.getmtime(path)))
        #Funkcja zwraca nam rozmiar danego pliku
        print('Size',os.path.getsize(path))
        #Informacja o bieżącym folderze
        print('Current folder',os.getcwd())
        #wyswietla wzgledna sciezke do pliku 
        print('Relative path to the file',os.path.relpath(path))
    else:
        print('%s must be file.'%file)