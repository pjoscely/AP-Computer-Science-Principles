#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:49:09 2020

@author: joscelynec
Given a 3X4 grid of SET cards, this program returns all valid 3 card SETS
 
"""

from itertools import combinations
puzzle = []

def welcome():
    print()
    print("************** Welcome to the SET Game Solver ****************\n")
    print("BLOCK 1   BLOCK 2  BLOCK 3 BLOCK 4\n")
    print("BLOCK 5   BLOCK 6  BLOCK 7 BLOCK 8\n")
    print("BLOCK 9   BLOCK 10  BLOCK 11 BLOCK 12\n")

    
    print("Each BLOCK accepts the following codes:\n")
    print("Shape: Ovals = ov, Squiggles = sq, Diamonds = di")
    print("Color: Red = re, Purple = pu, Green = gr")
    print("Number: One = 1,  Two = 2, Three = 3")
    print("Shading: Solid = so, Striped = st, Outlined = ot\n")
    print("When prompted please enter each BLOCK's code")
    
def fillPuzzle(puzzle):
    for i in range(1,13):
        block = str(input("Enter BLOCK "+ str(i)+":"))
        puzzle.append(block)
    print()
    
def displayPuzzle(puzzle):
    print("Below is your puzzle:\n")
    for i in range(0,3):
        for j in range(0,4):
            count = 4*i+j+1
            print("Block " + str(count)+" "+puzzle[count -1], end=" ")
        print()
    print()
    
    
    
def checkAttribute(a, b, c):
    if(a == b and b == c and a ==c):
        return True
    elif(a != b and b!=c and a != c):
        return True
    elif(a == b and a !=c):
        return False
    elif(a == c and a !=b):
        return False
    elif(b == c and a !=b):
        return False
    else:
        return False

  
    
def getThree(puzzle):
    return list(combinations(puzzle,3))

def formSet(threeTupleOfBlocks):
    b1 = threeTupleOfBlocks[0]
    b2 = threeTupleOfBlocks[1]
    b3 = threeTupleOfBlocks[2]
    
    b1Shape = b1[0:2]
    b1Color = b1[2:4]
    b1Num   = b1[4:5]
    b1Shade = b1[5:7]
    
    b2Shape = b2[0:2]
    b2Color = b2[2:4]
    b2Num  =  b2[4:5]
    b2Shade = b2[5:7]
    
    b3Shape = b3[0:2]
    b3Color = b3[2:4]
    b3Num   = b3[4:5]
    b3Shade = b3[5:7]
    
    if checkAttribute(b1Shape, b2Shape, b3Shape) and checkAttribute(b1Color, b2Color, b3Color) and checkAttribute(b1Num, b2Num, b3Num) \
    and checkAttribute(b1Shade, b2Shade, b3Shade):
        return True
    return False


def getAllSets(puzzle):
    print("Here are your SETS!\n")
    comb = getThree(puzzle)
    for c in comb:
        if(formSet(c)):
            print(c)            
    
welcome()
fillPuzzle(puzzle)
displayPuzzle(puzzle)
getAllSets(puzzle)