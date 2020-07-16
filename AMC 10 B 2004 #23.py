#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:00:00 2020

@author: joscelynec
"""
'''
This program uses Monte Carlo Simulation to solve an American Math Competition AMC
The problem is from the 2004 AMC 10B Problem 23

https://artofproblemsolving.com/wiki/index.php/2004_AMC_10B_Problems/Problem_23

Each face of a cube is painted either red or blue, each with probability 1/2. 
The color of each face is determined independently. What is the probability 
that the painted cube can be placed on a horizontal surface so that 
the four vertical faces are all the same color?

Solution: 5/16

The program simulates the problem scenario keeping track of the number of 
favorable outcomes. The ratio = favorables/(total trials) is computed and compared to 
the exact mathematical probability.


We model the cube as single die:
opposite faces are paired as (1,6), (2,5), (3,4)
here a cube is a list of lists, each of the six lists
are two element lits consisting of a value 1,2,3,4,5,6
and a color R, B or _ for intially no color

cube = [[1,'_'],[2,'_'],[3,'_'],[4,'_'],[5,'_'],[6,'_']]
'''


import random

'''
A utility method that given a cube
returns a random face with equal 
probability
''' 
def getFace(cube):
    rand_face = random.randint(0,5)
    return cube[rand_face]

'''
A utility method that assigns either R or B to a
cube's face with equal probability
recall a face is a two element lits [#,color]
''' 
def colorCube(cube):
    for face in cube:
        if(random.randint(0, 1) == 0):
            face[1] = 'R'
        else:
            face[1] = 'B'
    return cube

'''
A utility method that returns True 
if the supplied list_faces are of the same
color, False other wise
''' 
def sameColor(list_faces):
    init_color = list_faces[0][1]
    for i in range(1, len(list_faces)):
        if(list_faces[i][1] != init_color):
            return False
    return True

'''
A utility that given the cube and a face 
returns a list of the four adjacent faces
each face a list a two element list
containing a side number and color
'''             
def getAdjacent(cube, face):
    #construct a copy of the cube
    temp = []
    for f in cube:
        temp.append(f)
   
    #Remove the opposite side to face from temp
    if(face[0] == 1):
        #remove side 6
        temp.pop(5)
    elif(face[0] == 2):
        #remove side 5
        temp.pop(4)
    elif(face[0] == 3):
        #remove side 4
        temp.pop(3)
    elif(face[0] == 4):
        #remove side 3
        temp.pop(2)
    elif(face[0] == 5):
        #remove side 2
        temp.pop(1)
    else:
        #remove side 1
        temp.pop(0)
        
   #remove face from temp
    index = temp.index(face)
    temp.pop(index)
        
    #return temp a foru element list of adjacent faces to the original face
    return temp
'''
Main utility that given a random coloring returns 
True if cube can be placed on a horizontal surface so that 
the four vertical faces are all the same color
False otherwise
'''  

def canBePlace(cube):
    colorCube(cube) 
    for face in cube:
        temp = getAdjacent(cube, face)
        if(sameColor( temp)):
            return True
    return False

'''
We model the cube as single die:
opposite faces are paired as (1,6), (2,5), (3,4)
here a cube is a list of lists, each of the six lists
are two element lits consisting of a value 1,2,3,4,5,6
and a color R, B or _ for intially no color
'''
cube = [[1,'_'],[2,'_'],[3,'_'],[4,'_'],[5,'_'],[6,'_']]
'''
The mathematical solution from 
https://artofproblemsolving.com/wiki/index.php/2004_AMC_10B_Problems/Problem_23
lists 5/16 as the exact answer

A Monte Carlo simulation of 100000 trials is performed below 
the estimated and true value are then displayed 
'''
#set counter to zero
ct = 0 
#Start simulation
for j in range(100000):
#Color cube, place on horizontal surface and test 
    if(canBePlace(cube)):
        #if True incrmenet counter by 1
        ct+=1
    
#Display estimated and exact values
print(ct/100000,5/16)
'''
0.3126 0.3125
'''
    


