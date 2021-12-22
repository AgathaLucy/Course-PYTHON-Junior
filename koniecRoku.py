# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:03:58 2019

@author: 9
"""

def DaysToEndOfYear(year,month,day):
    from datetime import date
    date_today = date(year,month,day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
 
DaysToEndOfYear(2019,7,4)