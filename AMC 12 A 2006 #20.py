#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:35:31 2020

@author: joscelynec
"""
'''
This program uses Monte Carlo Simulation to solve an American Math Competition Problem AMC
The problem is from the 2006 AMC 12A Exam. Problem #20

A bug starts at one vertex of a cube and moves along the edges of the cube 
according to the following rule. At each vertex the bug will choose to travel 
along one of the three edges emanating from that vertex. 
Each edge has equal probability of being chosen, 
and all choices are independent. What is the probability 
that after seven moves the bug will have visited every vertex exactly once?
'''
import random

'''
Given a vertex move, randomly move along one of three edges of the unit cube
from the currentVertex to the nextVertex and return the nextVertex
the 8 vertices on the unit cube are represented as lists:
    
[0,0,0], [1,0,0], [0,1,0], ....., [1,1,1]

The function below randomly selects a coordinate in the currentVertex 
and then flips its bit. A new three element list called  nextVertex 
is created and returned.

****** Key Observations *****

On the unit cube a move along an edge 
can only change a single coordinate.

A move across a face would change two coordinates

A diagonal across the through the cube would change 
three coordinates.

****************************

'''
def getNextVertex(currentVertex):
    #randomly select x, y, z to change
    nextVertex = []
    c = random.randint(0,2)
    #a move to another vertex along an edge can only change a single coordinate
    #change the current value; 0 to 1, 1 to 0
    for i in range(3):
        if(i != c):
            nextVertex.append(currentVertex[i])
        else:
            if(currentVertex[c] == 0):
                 nextVertex.append(1)
            else:
                nextVertex.append(0)
        
    #return the next vertex
    return  nextVertex
'''
Begin at origin [0,0,0], perform a random walk of length 7 steps
return a list containg [0,0,0] and the subsequent 7 vertices
visted during the random walk
'''

def getWalk(startVertex):
    walk = []
    currentVertex = startVertex 
    for i in range(8):
        walk.append(currentVertex)
        currentVertex = getNextVertex(currentVertex)
    return walk
    
'''
Check if all 8 walk vertices are unique
There are slicker ways to do check,
but the program is aimed at AP CSP students.
Relies interestingly on the Pigeon Hole Principle
'''

def isWalkValid(walk):
    if([1,0,0] not in walk):
        return False
    elif([0,1,0] not in walk):
        return False
    elif([0,0,1] not in walk):
        return False
    elif([1,1,0] not in walk):
        return False
    elif([1,0,1] not in walk):
        return False
    elif([0,1,1] not in walk):
        return False
    elif([1,1,1] not in walk):
        return False
    else:
        return True
    
'''
The mathematical solution from 
https://artofproblemsolving.com/wiki/index.php/2006_AMC_12A_Problems/Problem_20 
lists 2/243 as the exact answer

A Monte Carlo simulation of 1000000 trials is performed below 
the estimated and true value are then displayed 

'''    
    
ct = 0   
for i in range(1000000):
    walk= getWalk([0,0,0])
    if(isWalkValid(walk)):
        ct+=1
print(ct/1000000, 2/243)

'''
Sample run

0.008265 0.00823045267489712
'''



