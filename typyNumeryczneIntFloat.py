# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:31:56 2019

@author: 9
"""

name = 'Bartek'
age = 26
daysInYear = 365
message = '%s is %d years old, so is about %d days old'

print(message%(name, age,age*daysInYear))

message1 = '{0:s} is {1:d} years old, so is about {2:d} days old'

print(message1.format(name, age,age*daysInYear))

aNumb = 1234567890 
bNumb = 12345
line = '{0:d} divided by {1:d} is  {2:d} and the rest is {3:d}'
print(line.format(aNumb,bNumb, aNumb//bNumb, aNumb%bNumb))