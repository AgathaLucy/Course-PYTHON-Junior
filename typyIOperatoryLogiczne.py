# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:08:29 2019

@author: 9
"""

isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = True

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
