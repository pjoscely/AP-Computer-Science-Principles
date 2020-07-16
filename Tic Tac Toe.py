#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:39:59 2020

@author: joscelynec
"""

#displays the grid
def displayBoard():
    global board
    print("  0 1 2" );
    for i in range(len(board)):
        temp = str(i)+" "
        for j in range(len(board)):
            temp+=board[i][j]+" "
        print(temp)
    print()

 
#This method returns true if space row, col is a valid space
def checkLocation(row, col):
    global board
    if((row >=0 and row< len(board) and (col>=0 and col< len(board)) and (board[row][col] == "_"))):
        return True
    return False

   
#This method places an X or O at location row,col based on the turn is even or odd
def takeTurn(row, col):
    global board
    global turn
    if(checkLocation(row,col) == False):
        print("Not a legal move.");
    # place an X if turn is even
    elif(turn %2 == 0):
        board[row][col] = "X"
        turn+=1;
    # place an O if turn is odd
    else:
        board[row][col] = "O"   
        turn+=1

#This method checks if a row has three X or O's in a row
def checkRow():
    global board
    for i in range(len(board)):
        temp = ""
        for j in range(len(board)):
            temp+=board[i][j]
        if(temp == "XXX" or temp == "OOO"):
            return True
    return False

#This method checks if a column has three X or O's
def checkCol():
    global board
    for i in range(len(board)):
        temp = ""
        for j in range(len(board)):
            temp+=board[j][i]
        if(temp == "XXX" or temp == "OOO"):
            return True
    return False


#This method checks if either diagonal has three X or O's
def checkDiag():
    global board
    diag1 =  board[0][0]+board[1][1]+board[2][2]
    diag2 =  board[0][2]+board[1][1]+board[2][0];
    if(diag1 == "XXX" or diag1 == "OOO"):
        return True
    if(diag2 == "XXX" or diag2 == "OOO"):
        return True
    
    return False
   
#This method checks if there is winner
def checkWin():
    global board
    if(checkRow() or checkCol() or checkDiag()):
        return True
      
    return False

#This method checks if there is tie
def checkTie():
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == "_"):
                return False
    return True
            
           
            
print("Let's play tic tac toe!")
player1 = str(input("Enter player 1's name:"))
player2 = str(input("Enter player 2's name:"))
print("Ok,",player1, "goes first.")

board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]
displayBoard()
turn = 0

while True:
    row = int(input("Please enter your row:"))
    col = int(input("Now enter your column:"))
    takeTurn(row, col)
    displayBoard()
    if(checkWin() and turn % 2 == 0):
        print(player1, "Wins!")
        break
    elif(checkWin() and turn % 2 == 1):
        print(player2, "Wins!")
        break
    elif(checkTie()):
        print("It's a Tie!")
        break
        
        
        







