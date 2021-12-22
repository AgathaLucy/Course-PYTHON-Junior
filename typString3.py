# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:37:58 2019

@author: 9
"""

article = '''
Monty Python (also collectively known as the Pythons)are a British surreal 
comedy group who created the sketch comedy television show Monty Python's 
Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were 
made over four series. The Python phenomenon developed from the television 
series into something larger in scope and impact, including touring stage 
shows, films, numerous albums, several books, and musicals. The Pythons' 
influence on comedy has been compared to the Beatles' influence on music.
Regarded as enduring icons of 1970s pop culture, their sketch show has been
referred to as being “an important moment in the evolution of television 
comedy".
'''

print(article.upper())
print(article.lower().replace('monty','flying'))
print(article.split(' '))
print('Word pyhton appears %d times.'%article.count('Python'))
print(r'to print the \ you need to put \ twice in your text like this: \\')
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

print('\n')

amountPLN = 234
print('cur\texchange\tamount')
print('USD\t%f\t%f'%(3.65,amountPLN/3.65))
print('EUR\t%f\t%f'%(4.23,amountPLN/4.23))

print('\n')

valueAsTest = '123.45'
factor = 1.23

print('value is',valueAsTest,'factor is',str(factor),'value*factor=',str(float(valueAsTest)*factor))