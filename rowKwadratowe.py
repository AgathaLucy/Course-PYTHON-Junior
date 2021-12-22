# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:25:49 2019

@author: 9
"""
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print("The program will calculate the quadratic equation for given parameters.")
while True:
    
    str_a=input("Enter the first intiger:")
    str_b=input("Enter the second intiger:")
    str_c=input("Enter the third intiger:")
    
    if not(check_int(str_a) and check_int(str_b) and check_int(str_c)):
        print("The numbers are not TOTAL!!!")
        break
    else:
        num_a=int(str_a)
        num_b=int(str_b)
        num_c=int(str_c)
        if num_a==0:
            print("It is not quadratic equation.")
            break
        else:
            delta=pow(num_b,2)-(4*num_a*num_c)
            print("\nDelta równa się: %s."%delta)
            if delta<0:
                print("No solutions.")
            elif delta==0:
                x1=(-num_b-pow(delta,0.5))/2*num_a
                print(x1)
            elif delta>0:
                x1=(-num_b-pow(delta,0.5))/2*num_a
                x2=(num_b-pow(delta,0.5))/2*num_a
                print(x1)
                print(x2)
            break