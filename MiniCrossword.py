#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:10:14 2020

@author: joscelynec
"""


puzzle = [['####','1___','2___','3___',' ####\n'], 
          ['4___','____','____','____','5___\n'], 
          ['6___','____','____','____','____\n'],
          ['7___','____','____','____','____\n'],
          ['####','____','____','____','####\n']]
          
          
solution = [['###','D','I','P','###'], 
         ['L','A','R','R','Y'], 
         ['A','V','O','I','D'],
         ['W','I','N','D','S'],
         ['###','D','Y', 'E','###']]          
          

num_correct = 0  
num_computer = 0         
          

def welcome():
    print()
    print("************** Welcome to MINI CROSSWORD ****************\n")
    print("Rows are horizontal, numbered 0 to 4; Columns are vertical, numbered 0 to 4")
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


def printClues():
    print()
    print("ACROSS")
    print("1 Quick swim")
    print("4 With 1-Down, star of 'Curb Your Enthusiasm'")
    print("6 Steer clear of")
    print("7 Hurricanes have strong ones")
    print("8 Easter egg coloring")
    print()
    print("DOWN")
    print("1 See 4-Across")
    print("2 Kind of humor much seen in postmodernism")
    print("3 Group of lions")
    print("4 Postgraduate field")
    print("5 Golf hole measure: Abbr")
    
    
printClues()  





  
 
def check(puzzle):
    global num_correct
    global num_computer
    row = int(input("Enter row:"))
    col = int(input("Enter col:"))
    letter = str(input("Enter letter or type hint:"))
    if (letter == "hint"):
        letter = solution[row][col]
        puzzle[row][col] = (puzzle[row][col])[0:2]+letter+(puzzle[row][col])[3:]
        printPuzzle(puzzle)
        printClues()   
    elif(solution[row][col] != letter.upper()):
        print("Sorry, please try a different letter")
        printPuzzle(puzzle)
        printClues()
    else:
        puzzle[row][col] = (puzzle[row][col])[0:2]+letter.upper()+(puzzle[row][col])[3:]
        num_correct+=1
        printPuzzle(puzzle)
        printClues()
    
while((num_correct + num_computer)<21):
    check(puzzle)
print()
print("You solved the puzzle!")
print("Computer solved "+ str(num_computer)+" letters.")
    
