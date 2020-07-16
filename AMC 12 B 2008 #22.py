#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:59:52 2020

@author: joscelynec

This program uses Monte Carlo Simulation to solve an American Math Competition AMC
The problem is from the 2008 AMC 12B Problem 22

https://artofproblemsolving.com/wiki/index.php/2008_AMC_12B_Problems/Problem_22

A parking lot has 16 spaces in a row. Twelve cars arrive, each of which requires one parking space, 
and their drivers chose spaces at random from among the available spaces. 
Auntie Em then arrives in her SUV, which requires 2 adjacent spaces. 
What is the probability that she is able to park?

Solution: 17/28

The program simulates the problem scenario keeping track of the number of 
favorable outcomes. The ratio = favorables/(total trials) is computed and compared to 
the exact mathematical probability.

"""
import random
#returns a list of all parking configurations
def getRandomLot(lot):
    random.shuffle(lot)
    return lot

#returns true if their is a pair of adjacent zeros 0,0 in the lot
def isValidLot(lot):
    for i in range(len(lot)-1):
        if(lot[i] == 0 and lot[i+1] == 0):
            return True
    return False
            
'''
The mathematical solution from 
https://artofproblemsolving.com/wiki/index.php/2008_AMC_12B_Problems/Problem_22
lists 17/28 as the exact answer

A Monte Carlo simulation of 1000000 trials is performed below 
the estimated and true value are then displayed 

'''
lot = [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]

ct = 0   
for i in range(100000):
    if(isValidLot(getRandomLot(lot))):
        ct+=1
print(ct/100000, 17/28)


'''
A sample result for 1000000 trials:
0.607486 0.6071428571428571
'''  
    





