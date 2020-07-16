#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:55:08 2020

@author: joscelynec

This program uses Monte Carlo Simulation to solve an American Math Competition Problem AMC
The problem is from the 2019 AMC 12A #16

The numbers 1,2,..,9 are randomly placed into the 9 squares of a 3 by 3 grid. 
Each square gets one number, and each of the numbers is used once. 
What is the probability that the sum of the numbers in each row and each column is odd?

The program simulates the problem scenario keeping track of the number of 
favorable outcomes. The ratio = favorables/(total trials) is computed and compared to 
the exact mathematical probability.

"""
import random 
grid = [[0,0,0], [0,0,0], [0,0,0]]
digits =[1,2,3,4,5,6,7,8,9]

#displays the grid
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end =" ")
        print()
        
#fills grid with randomly placed digits
def fillGrid(grid, digits):
    random.shuffle(digits)
    indx = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = digits[indx]
            indx+=1
    return grid

#Returns row sum          
def rowSum(grid, row):
    sum = 0
    for col in range(len(grid)):
        sum+=grid[row][col]
    return sum    

#Returns column sum  
def colSum(grid, col):
    sum = 0
    for row in range(len(grid)):
        sum+=grid[row][col]
    return sum

#Parity check
def isOdd(num):
    if(num%2 == 1):
        return True
    else:
        return False

'''
Monte Carlo Simulation
'''
numTimes = 0
for i in range(100000): 
    grid = fillGrid(grid, digits)
  
    if(isOdd(rowSum(grid,0)) and isOdd(rowSum(grid,1)) and isOdd(rowSum(grid,2)) and isOdd(colSum(grid,0)) and isOdd(colSum(grid,1)) and isOdd(colSum(grid,2))):
        numTimes+=1

print(numTimes/100000,1/14)

'''
A sample result for 100000 trials:
0.07095 0.07142857142857142
'''  
    
    
    











