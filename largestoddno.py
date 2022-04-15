#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:26:07 2021

@author: jagpreet
"""

n1 = int (input('enter ten integers : '))
n2 = int (input('enter ten integers : '))
n3 = int (input('enter ten integers : '))
n4 = int (input('enter ten integers : '))
n5 = int (input('enter ten integers : '))
n6 = int (input('enter ten integers : '))
n7 = int (input('enter ten integers : '))
n8 = int (input('enter ten integers : '))
n9 = int (input('enter ten integers : '))
n10 = int (input('enter ten integers : '))

while True :
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0 and n5%2==0 and n6%2==0 and n7%2==0 and n8%2==0 and n9%2==0 and n10%2==0 :
        print('no odd numbers :')
        break
    elif n1%2==1 and n1>n2 and n1>n3 and n1>n4 and n1>n5 and n1>n6 and n1>n7 and n1>n8 and n1>n9 and n1>n10 :
            print('largest odd number: ' + str(n1))
            break
    elif n2%2==1 and n2>n1 and n2>n3 and n2>n4 and n2>n5 and n2>n6 and n2>n7 and n2>n8 and n2>n9 and n2>n10 :
            print('largest odd number: ' + str(n2))
            break
    elif n3%2==1 and n3>n1 and n3>n2 and n3>n4 and n3>n5 and n3>n6 and n3>n7 and n3>n8 and n3>n9 and n3>n10 :
            print('largest odd number: ' + str(n3))
            break
              
    elif n4%2==1 and n4>n1 and n4>n2 and n4>n3 and n4>n5 and n4>n6 and n4>n7 and n4>n8 and n4>n9 and n4>n10 :
            print('largest odd number: ' + str(n4))
            break
    elif n5%2==1 and n5>n2 and n5>n3 and n5>n4 and n1<n5 and n5>n6 and n5>n7 and n5>n8 and n5>n9 and n5>n10 :
            print('largest odd number: ' + str(n5))
            break
              
    elif n6%2==1 and n6>n2 and n6>n3 and n6>n4 and n6>n5 and n1<n6 and n6>n7 and n6>n8 and n6>n9 and n6>n10 :
            print('largest odd number: ' + str(n6))
            break
              
    elif n7%2==1 and n7>n2 and n7>n3 and n7>n4 and n7>n5 and n7>n6 and n1<n7 and n7>n8 and n7>n9 and n7>n10 :
            print('largest odd number: ' + str(n7))
            break
              
    

   
   
    
    elif n8%2==1 and n8>n2 and n8>n3 and n8>n4 and n8>n5 and n8>n6 and n8>n7 and n8>n1 and n8>n9 and n8>n10 :
            print('largest odd number: ' + str(n8))
            break
    elif n9%2==1 and n9>n2 and n9>n3 and n9>n4 and n9>n5 and n9>n6 and n9>n7 and n9>n8 and n9>n1 and n9>n10 :
            print('largest odd number: ' + str(n9))
            break
    elif n10%2==1 and n10>n1 and  n10>n2 and n10>n3 and n10>n4 and n10>n5 and n10>n6 and n10>n7 and n10>n8 and n10>n9 :
            print('largest odd number: ' + str(n10))
            break
    
    
    
        
