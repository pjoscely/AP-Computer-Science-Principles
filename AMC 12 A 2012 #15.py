#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:09:12 2020

@author: joscelynec
This program uses Monte Carlo Simulation to solve an American Math Competition Problem AMC
The problem is from the 2012 AMC Test 12A #15

A 3 by 3 square is partitioned into 9 unit squares. 
Each unit square is painted either white or black with each color being equally likely, 
chosen independently and at random. The square is then rotated 90 deg clockwise 
about its center, and every white square in a position 
formerly occupied by a black square is painted black. 
The colors of all other squares are left unchanged. 
What is the probability that the grid is now entirely black?

The program simulates the problem scenario keeping track of the number of 
favorable outcomes. The ratio = favorables/(total trials) is computed and compared to 
the exact mathematical probability.
"""
import random 

#displays the grid
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end =" ")
        print()
    print()
       
#fills grid with  or 'W' with each color equally 
def fillGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(random.random() < .5):
                grid[i][j] = 'B'
            else:
                grid[i][j] = 'W'
    return grid

#Returns a rotated grid
def rotate(grid):
    rotatedGrid = [['_','_','_'], ['_','_','_'], ['_','_','_']]
    rotatedGrid[0][0] = grid[2][0]
    rotatedGrid[0][1] = grid[1][0]
    rotatedGrid[0][2] = grid[0][0]
    rotatedGrid[1][2] = grid[0][1]
    rotatedGrid[2][2] = grid[0][2]
    rotatedGrid[2][1] = grid[1][2]
    rotatedGrid[2][0] = grid[2][2]
    rotatedGrid[1][0] = grid[2][1]
    rotatedGrid[1][1] = grid[1][1]
    return rotatedGrid

#Returns a repainted grid as described in the problem
def repaint(grid):
    rot = rotate(grid);
    if(rot[0][0] == 'W' and grid[0][0] == 'B'):
        rot[0][0] = 'B'
    if(rot[0][1] == 'W' and grid[0][1] == 'B'):
        rot[0][1] = 'B'
    if(rot[0][2] == 'W' and grid[0][2] == 'B'):
        rot[0][2] = 'B'
    if(rot[1][2] == 'W' and grid[1][2] == 'B'):
        rot[1][2] = 'B'
    if(rot[2][2] == 'W' and grid[2][2] == 'B'):
        rot[2][2] = 'B'
    if(rot[2][1] == 'W' and grid[2][1] == 'B'):
        rot[2][1] = 'B'
    if(rot[2][0] == 'W' and grid[2][0] == 'B'):
        rot[2][0] = 'B'
    if(rot[1][0] == 'W' and grid[1][0] == 'B'):
        rot[1][0] = 'B'
    return rot
    
#Returns True if grid is entirely black, False otherwise
def checkBlack(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 'W'):
                return False
    return True
    
#Monte Carlo Simulation 
numTimes = 0
for i in range(100000):
    #create empty 3x3 grid
    grid = [['_','_','_'], ['_','_','_'], ['_','_','_']]
    #fill grid
    fillGrid(grid)
    if(checkBlack(repaint(grid))):
        numTimes+=1

#Display the estimated and true probability after 100000 trials
print(numTimes/100000, 49/512)
    
'''
A sample result for 100000 trials:
0.09564 0.095703125
'''       

    







  