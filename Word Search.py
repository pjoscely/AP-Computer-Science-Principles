#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:59:59 2020

@author: joscelynec
This program finds a list of words in a grid. Words may be found in any
of the 8 compass dirctions
"""
'''
Word finds puzzle for XMAS words list below

V A D M T X R A N G I F T C Z N S H F Q 
S U A L C A T N A S O D M Z U F O C V S 
D E Y C L C N L B F Q I N R K T L O Y T 
N Q P O H S L E I G H P H E U J N K N N 
A V F U N I J V L V P U C I W K M Q O I 
L D Z S Y O M C D U L C O N R R I Q I C 
R A L L E U R N O V O Z S D E I L U T K 
A S L Z C O S T E H D M C E A S K G A Y 
G H B S S M T X H Y U Q U E T S A R R N 
M E B L I T Z E N P R F H R H K N R O P 
N R R Z N T N C L M O E N U U R D E C O 
T Y Z E W B E I W T T L E H T I C C E F 
P A Z E C M A E C B S C E L N N O N D L 
V J L Y N N P Y R H A I U E E G O A K E 
P E D P Z R A E O L O M M R M L K R R S 
O E Q M E L N D P K L L A J A E I P P N 
U L M S F N S E V E F C A R N M E V W I 
Q J E I O W R U C U C V C S R H S U C T 
M N I D O I V I X E N I P R O C J B V C 
T C D O F E G G N O G X I C O M E T W A 
'''

from time import sleep

words = ['BLITZEN', 'CHIMNEY', 'COMET', 'CUPID', 'DANCER', 'DASHER', 'DECORATION', 'DONNER', 
         'EGGNOG', 'FIREPLACE', 'GARLAND', 'GIFT', 'KRISS KRINGLE', 'MILK AND COOKIES',
         'MISTLETOE', 'NORTH POLE', 'ORNAMENT', 'PRANCER', 'PRESENT', 'REINDEER', 'RUDOLPH', 
         'SANTA CLAUS', 'SLEIGH', 'ST NICHOLAS', 'ST NICK', 'TINSEL', 'VIXEN', 'WREATH']


puzzle = [['V', 'A', 'D', 'M', 'T', 'X', 'R', 'A', 'N', 'G', 'I', 'F', 'T', 'C', 'Z', 'N', 'S', 'H', 'F', 'Q'], 
          ['S', 'U', 'A', 'L', 'C', 'A', 'T', 'N', 'A', 'S', 'O', 'D', 'M', 'Z', 'U', 'F', 'O', 'C', 'V', 'S'], 
          ['D', 'E', 'Y', 'C', 'L', 'C', 'N', 'L', 'B', 'F', 'Q', 'I', 'N', 'R', 'K', 'T', 'L', 'O', 'Y', 'T'], 
          ['N', 'Q', 'P', 'O', 'H', 'S', 'L', 'E', 'I', 'G', 'H', 'P', 'H', 'E', 'U', 'J', 'N', 'K', 'N', 'N'], 
          ['A', 'V', 'F', 'U', 'N', 'I', 'J', 'V', 'L', 'V', 'P', 'U', 'C', 'I', 'W', 'K', 'M', 'Q', 'O', 'I'], 
          ['L', 'D', 'Z', 'S', 'Y', 'O', 'M', 'C', 'D', 'U', 'L', 'C', 'O', 'N', 'R', 'R', 'I', 'Q', 'I', 'C'], 
          ['R', 'A', 'L', 'L', 'E', 'U', 'R', 'N', 'O', 'V', 'O', 'Z', 'S', 'D', 'E', 'I', 'L', 'U', 'T', 'K'], 
          ['A', 'S', 'L', 'Z', 'C', 'O', 'S', 'T', 'E', 'H', 'D', 'M', 'C', 'E', 'A', 'S', 'K', 'G', 'A', 'Y'], 
          ['G', 'H', 'B', 'S', 'S', 'M', 'T', 'X', 'H', 'Y', 'U', 'Q', 'U', 'E', 'T', 'S', 'A', 'R', 'R', 'N'], 
          ['M', 'E', 'B', 'L', 'I', 'T', 'Z', 'E', 'N', 'P', 'R', 'F', 'H', 'R', 'H', 'K', 'N', 'R', 'O', 'P'], 
          ['N', 'R', 'R', 'Z', 'N', 'T', 'N', 'C', 'L', 'M', 'O', 'E', 'N', 'U', 'U', 'R', 'D', 'E', 'C', 'O'], 
          ['T', 'Y', 'Z', 'E', 'W', 'B', 'E', 'I', 'W', 'T', 'T', 'L', 'E', 'H', 'T', 'I', 'C', 'C', 'E', 'F'], 
          ['P', 'A', 'Z', 'E', 'C', 'M', 'A', 'E', 'C', 'B', 'S', 'C', 'E', 'L', 'N', 'N', 'O', 'N', 'D', 'L'], 
          ['V', 'J', 'L', 'Y', 'N', 'N', 'P', 'Y', 'R', 'H', 'A', 'I', 'U', 'E', 'E', 'G', 'O', 'A', 'K', 'E'], 
          ['P', 'E', 'D', 'P', 'Z', 'R', 'A', 'E', 'O', 'L', 'O', 'M', 'M', 'R', 'M', 'L', 'K', 'R', 'R', 'S'], 
          ['O', 'E', 'Q', 'M', 'E', 'L', 'N', 'D', 'P', 'K', 'L', 'L', 'A', 'J', 'A', 'E', 'I', 'P', 'P', 'N'], 
          ['U', 'L', 'M', 'S', 'F', 'N', 'S', 'E', 'V', 'E', 'F', 'C', 'A', 'R', 'N', 'M', 'E', 'V', 'W', 'I'], 
          ['Q', 'J', 'E', 'I', 'O', 'W', 'R', 'U', 'C', 'U', 'C', 'V', 'C', 'S', 'R', 'H', 'S', 'U', 'C', 'T'], 
          ['M', 'N', 'I', 'D', 'O', 'I', 'V', 'I', 'X', 'E', 'N', 'I', 'P', 'R', 'O', 'C', 'J', 'B', 'V', 'C'], 
          ['T', 'C', 'D', 'O', 'F', 'E', 'G', 'G', 'N', 'O', 'G', 'X', 'I', 'C', 'O', 'M', 'E', 'T', 'W', 'A']]

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

#Displays if word was found, then display location and direction
for word in words:
    w = word.replace(" ", "")
    search(puzzle,w)
    sleep(.5)