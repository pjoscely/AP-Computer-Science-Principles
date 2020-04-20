#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:59:59 2020

@author: joscelynec
This program finds a list of words in a grid. Words may be found in any
of the 8 compass dirctions
"""
'''
E N G G H L M E K C L G V S E
Q L C R C Z R E S R E H F E X
U D O L E O F L U N D R Z P N
W D C O O B T S Z K Q H J M M
O S J M B U R R K U T N P U P
Z R E R R T R E P O O H S E Z
N C I I N J Z N K V J S E V B
I N N J K I Z R P C O C T P S
A G B Y O U P E J R U V A A W
K L S A F B P B N S T Z G G Z
Z T I H B D S A M W T O R E B
F P R Y E B V C F I B K Q I K
N G E I O W A H J N W Q L F H
H E J C F I F G K N U T H A N
'''

from time import sleep
#Famous CS people
words =["BABBAGE","BERNERSLEE","BOOLE","BRIN","GATES","HOOPER","JOBS","KNUTH",
"LOVELACE","PAGE","TURING","WOZNIAK","ZUCKERBERG","MOORE","VANROSSUM"]

puzzle = [["E", "N", "G", "E", "H", "L", "M", "E", "K", "C", "L", "G", "V", "S", "E"],
["Q", "L", "C", "R", "C", "Z", "R", "E", "S", "R", "E", "H", "F", "E", "X"],
["U", "D", "O", "O", "E", "O", "F", "L", "U", "N", "D", "R", "Z", "P", "N"],
["W", "D", "C", "O", "O", "B", "T", "S", "Z", "K", "Q", "H", "J", "M", "M"],
["O", "S", "J", "M", "B", "U", "R", "R", "K", "U", "T", "N", "P", "U", "P"],
["Z", "R", "E", "R", "R", "T", "R", "E", "P", "O", "O", "H", "S", "E", "Z"],
["N", "C", "I", "I", "N", "J", "Z", "N", "K", "V", "J", "S", "E", "V", "B"],
["I", "N", "N", "J", "K", "I", "Z", "R", "P", "C", "O", "C", "T", "P", "S"],
["A", "G", "B", "Y", "O", "U", "P", "E", "J", "R", "U", "V", "A", "A", "W"],
["K", "L", "S", "A", "F", "B", "P", "B", "N", "S", "T", "Z", "G", "G", "Z"],
["Z", "T", "I", "H", "B", "D", "S", "A", "M", "W", "T", "O", "R", "E", "B"],
["F", "P", "R", "Y", "E", "B", "V", "C", "F", "I", "B", "K", "Q", "I", "K"],
["N", "G", "E", "I", "O", "W", "A", "H", "J", "N", "W", "Q", "L", "F", "H"],
["H", "E", "J", "C", "F", "I", "F", "G", "K", "N", "U", "T", "H", "A", "N"],
["Q", "L", "O", "V", "E", "L", "A", "C", "E", "B", "G", "M", "V", "L", "T"]]


#Checks if a location i, j is valid
def isValid(puzzle, i, j):
    return (0<=i and i <len(puzzle) and 0<=j and j <len(puzzle))


#Main algorithm SEARCHES IN 8 COMPASS DIRECTIONS AROUND A LETTER
def search(puzzle,word):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if(puzzle[i][j]==word[0]):
                if(searchN(puzzle,i,j,word)):
                    print(word,"found at",i,j,"N")
                    return
                elif(searchENE(puzzle,i,j,word)):
                    print(word,"found at",i,j,"ENE")
                    return
                elif(searchE(puzzle,i,j,word)):
                    print(word,"found at",i,j,"E")
                    return
                elif(searchESE(puzzle,i,j,word)):
                    print(word,"found at",i,j,"ESE")
                    return
                elif(searchS(puzzle,i,j,word)):
                    print(word,"found at",i,j,"S")
                    return
                elif(searchWSW(puzzle,i,j,word)):
                    print(word,"found at",i,j,"WSW")
                    return
                elif(searchW(puzzle,i,j,word)):
                    print(word,"found at",i,j,"W")
                    return
                elif(searchWNW(puzzle,i,j,word)):
                    print(word,"found at",i,j,"WNW")
                    return
    print(word,"Not found")

'''
Search at the 8 compass directions 
'''
def searchN(puzzle,i,j,word):
    N = i-1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,N,j) or (puzzle[N][j] != word[pos])):
            return False
        N-=1
        pos+=1
    return True


def searchENE(puzzle,i,j,word):
    E = j+1
    N = i-1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,N,E) or (puzzle[N][E] != word[pos])):
            return False
        E+=1
        N-=1
        pos+=1
    return True


def searchE(puzzle,i,j,word):
    E = j+1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,i,E) or (puzzle[i][E] != word[pos])):
            return False
        E+=1
        pos+=1
    return True


def searchESE(puzzle,i,j,word):
    E = i+1
    S = j+1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,E,S) or (puzzle[E][S] != word[pos])):
            return False
        S+=1
        E+=1
        pos+=1
    return True


def searchS(puzzle,i,j,word):
    S = i+1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,S,j) or (puzzle[S][j] != word[pos])):
            return False
        S+=1
        pos+=1
    return True

def searchWSW(puzzle,i,j,word):
    S = i+1
    W = j-1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,S,W) or (puzzle[S][W] != word[pos])):
            return False
        S+=1
        W-=1
        pos+=1
    return True


def searchW(puzzle,i,j,word):
    W = j-1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,i,W) or (puzzle[i][W] != word[pos])):
            return False
        W-=1
        pos+=1
    return True


def searchWNW(puzzle,i,j,word):
    N = i-1
    W = j-1
    pos = 1
    while pos < len(word):
        if(not isValid(puzzle,N,W) or (puzzle[N][W] != word[pos])):
            return False
        N-=1
        W-=1
        pos+=1
    return True


for w in words:
    search(puzzle,w)
    sleep(.5)
