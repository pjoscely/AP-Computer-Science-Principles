#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:59:52 2020

@author: joscelynec


This program uses Monte Carlo Simulation to solve an American Math Competition AMC
The problem is from the 2010 AMC 12A Exam Problem 16


Bernardo randomly picks 3 distinct numbers from the set {1,2,3,4,5,6,7,8,9}
and arranges them in descending order to form a 3-digit number. 
Silvia randomly picks 3 distinct numbers from the set 
{1,2,3,4,5,6,7,8} and also arranges them in descending order 
to form a 3-digit number. What is the probability that Bernardo's 
number is larger than Silvia's number?

The program simulates the problem scenario keeping track of the number of 
favorable outcomes. The ratio = favorables/(total trials) is computed and compared to 
the exact mathematical probability.

"""

import random

#returns decimal value of a 3 digit list
def getDecimalVal(lst):
    return 100*lst[0] + 10*lst[1] + lst[2]


#returns a Bernardo number
def getBernardoNUM():
    bernardoDigits = [1,2,3,4,5,6,7,8,9]
    bernardoThree = []
    for i in range(3):
        random.shuffle(bernardoDigits)
        bernardoThree.append(bernardoDigits.pop())
    bernardoThree.sort(reverse=True)
    return getDecimalVal(bernardoThree)
          
    
#returns a Silvia number    
def getSilviaNUM():
    silviaDigits = [1,2,3,4,5,6,7,8]
    silviaThree = []
    for i in range(3):
        random.shuffle(silviaDigits)
        silviaThree.append(silviaDigits.pop())
    silviaThree.sort(reverse=True)
    return getDecimalVal(silviaThree)
    
'''
The mathematical solution from 
https://artofproblemsolving.com/wiki/index.php/2010_AMC_12A_Problems/Problem_16
lists 37/56 as the exact answer

A Monte Carlo simulation of 1000000 trials is performed below 
the estimated and true value are then displayed 

'''
ct = 0   
for i in range(1000000):
    if(getBernardoNUM() > getSilviaNUM()):
        ct+=1
print(ct/1000000, 37/56)


'''
A sample result for 100000 trials:
0.66123 0.6607142857142857
'''  
    





