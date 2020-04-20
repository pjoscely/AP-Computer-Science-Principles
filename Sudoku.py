#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:33:11 2020

@author: joscelynec
"""

puzzle = [['___','___','||',' 1 ','___'], 
          [' 2 ',' 1 ','||',' 4 ','___'],
          ['===','===','||','===','==='],
          [' 1 ',' 2 ','||',' 3 ','___'],
          [' 3 ','___','||',' 2 ','___']]
           
def welcome():
    print()
    print("************** Welcome to MINI 4x4 Sudoku ****************\n")
    print(" BLOCK 1   BLOCK 2 \n")
    print(" BLOCK 3   BLOCK 4 \n")
    
    print("Enter your BLOCK: 1, 2, 3, 4\n")
    print("Enter the row: 0, 1 and column: 0, 1 within the block\n")
    print("Below is you puzzle. Good luck!")
welcome()

#displays the puzzle
def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        print()
        for j in range(len(puzzle)):
            print(puzzle[i][j],end=' ')
        print()
    print()
        
printPuzzle(puzzle)

def check_block(puzzle,block,guess):
    
    
    if(block == 1):
        s = str(puzzle[0][0])+str(puzzle[0][1])+str(puzzle[1][0])+str(puzzle[1][1])
       
    elif(block == 2):
        s = str(puzzle[0][3])+str(puzzle[0][4])+str(puzzle[1][3])+str(puzzle[1][4])
        
    
    elif(block == 3):
        s = str(puzzle[3][0])+str(puzzle[3][1])+str(puzzle[4][0])+str(puzzle[4][1])
      
    else:
           s = str(puzzle[3][3])+str(puzzle[3][4])+str(puzzle[4][3])+str(puzzle[4][4])
    
    if(str(guess) in s):
        return False
    else:
        return True  
    
def check_row(puzzle,block,row,guess):
    if(block == 1 or block == 2):
        s = str(puzzle[row][0])+str(puzzle[row][1])+str(puzzle[row][3])+str(puzzle[row][4])
    else:
        s = str(puzzle[row+3][0])+str(puzzle[row+3][1])+str(puzzle[row+3][3])+str(puzzle[row+3][4])
        
    if(str(guess) in s):
        return False
    else:
        return True



def check_col(puzzle,block, col,guess):
     if(block == 1 or block ==3):
         s = str(puzzle[0][col])+str(puzzle[1][col])+str(puzzle[3][col])+str(puzzle[4][col])
     else:
         s = str(puzzle[0][col+3])+str(puzzle[1][col+3])+str(puzzle[3][col+3])+str(puzzle[4][col+3])
     
     if(str(guess) in s):
        return False
     else:
        return True

       

def check(puzzle,block, row, col, guess):
    if (check_block(puzzle,block, guess) == False ):
        return False
    if (check_row(puzzle,block, row, guess) == False ):
        return False
    if (check_col(puzzle,block,col, guess) == False ):
        return False
    return True

def update(puzzle,block, row, col,guess):
    if(block == 1):
        puzzle[row][col] = " "+str(guess)+" "
    elif(block == 2):
        puzzle[row][col+3] = " "+str(guess)+" "
    elif(block == 3):
        puzzle[row+3][col] = " "+str(guess)+" "
    else:
        puzzle[row+3][col+3] = " "+str(guess)+" "
def Solved(puzzle):
    s =''
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            s+=puzzle[i][j]
    if('___' in s):
        return False
    else:
        return True
        


def guess(puzzle):
    block = int(input("Enter block:"))
    row = int(input("Enter row:"))
    col = int(input("Enter col:"))
    guess = int(input("Enter guess:"))
    if(check(puzzle,block, row, col,guess)):
        update(puzzle,block, row, col,guess)
        printPuzzle(puzzle) 
    else:
        print("Illegal move, try again")
 
while(True):
    guess(puzzle)
    if(Solved(puzzle)):
        print("You solved the puzzle!")
        break
       
        
        
        
        
    