# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:07:17 2019

@author: 9
"""
#Zad 1
#initialCapital = 20000
#percent = 0.03
#maxTimeYears = 10
#interest = 0
#allInterest = 0
#year = 1
#while year <= maxTimeYears:
#    interest = initialCapital*percent
#    allInterest+=interest
#    initialCapital+=interest
#    print('W roku %2d odsetki wyniosły: %4d.'% (year,interest))
#    year+=1
#print('Cała zarobiona kwota w naszym banku to: %d.' % (allInterest))

#Zad 2
#number = 20730906
#i = 1
#suma = 0
#div=10
#while i<=8:
#    suma+=number%div
#    number=number//div
#    i+=1
#print(suma)

#Zad 3
text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''

wordLength = 6
listOfWords = text.replace('\n',' ').split(' ')
shortWords = 0
longWords = 0
i = 0
while i < len(listOfWords):
    word = listOfWords[i]
    if len(word)>=wordLength:
        longWords+=1
    elif len(word)<wordLength and len(word)>0:
        shortWords+=1
    i+=1
print('Słow dłuższych niż %d jest w tekcie %d, a krótszych %d.'%(wordLength,longWords,shortWords))
    
    