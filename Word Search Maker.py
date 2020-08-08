#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:33:19 2020

@author: joscelynec
"""
'''
Given a list of words this program creates a random WORD SEARCH puzzle
Words may be placed in any of the eight compass dirctions

For example can be found in the directions:
N, ENE, E, ESE, S, WSW, W, WNW
         
        E    E    E 
         L   L   L
          Z  Z  Z
           Z Z Z
            UUU
        ELZZUPUZZLE
            UUU           
           Z Z Z
          Z  Z  Z
         L   Z   L
        E    L    E
             E

'''
import random 
import string
from time import sleep

#list of words to be placed in the Word Search 
#Replace with your own
words = ['BLITZEN', 'CHIMNEY', 'COMET', 'CUPID', 'DANCER', 'DASHER', 'DECORATION', 'DONNER', 
         'EGGNOG', 'FIREPLACE', 'GARLAND', 'GIFT', 'KRISS KRINGLE', 'MILK AND COOKIES',
         'MISTLETOE', 'NORTH POLE', 'ORNAMENT', 'PRANCER', 'PRESENT', 'REINDEER', 'RUDOLPH', 
         'SANTA CLAUS', 'SLEIGH', 'ST NICHOLAS', 'ST NICK', 'TINSEL', 'VIXEN', 'WREATH']

#displays the grid
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end =" ")
        print()
    print()
'''
For each word in word list remove all white space 
Pick a random position in the grid
Explore at random all eight compass positions
N, ENE, E, ESE, S, WSW, W, WNW  in an attempt to place
the word. If successfull, place the word and 
repeat on the next word. If unable to place the word 
repeat the process at a new random position until 
the word is successfully placed in the grid.

Note: The eight functions should be consolidated 
into a single function but are presented as is
for student practice in function writing. 
'''

#Try to place word to the North
def tryPlaceN(grid,i,j,word):
    #remove white space
    w = word.replace(" ", "")
    #Is there room to the north
    if(i+1 - len(w) < 0):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i-indx][j] != w[indx] and grid[i-indx][j] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i-indx][j] = w[indx]
    return True

#Try to place word to the East North East   
def tryPlaceENE(grid,i,j,word):
    #remove white space
    w = word.replace(" ", "")
    #Is there room to the East North East
    if(i+1 - len(w) < 0 or len(grid) -j - len(w) < 0 ):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i-indx][j+indx] != w[indx] and grid[i-indx][j+indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i-indx][j+indx] = w[indx]
    return True       
    
#Try to place word to the East    
def tryPlaceE(grid,i,j,word):
    #remove white space
    w = word.replace(" ", "")
    #Is there room to the East
    if(len(grid) -j - len(w) < 0):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i][j+indx] != w[indx] and grid[i][j+indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i][j+indx] = w[indx]
    return True
    
#Try to place word to the East South East 
def tryPlaceESE(grid,i,j,word):
      #remove white space
    w = word.replace(" ", "")
    #Is there room to the East South East
    if(len(grid) -i - len(w) < 0 or len(grid) -j - len(w) < 0 ):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i+indx][j+indx] != w[indx] and grid[i+indx][j+indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i+indx][j+indx] = w[indx]
    return True

#Try to place word to the South   
def tryPlaceS(grid,i,j,word):
      #remove white space
    w = word.replace(" ", "")
    #Is there room to the South
    if(len(grid) -i - len(w) < 0):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i+indx][j] != w[indx] and grid[i+indx][j] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i+indx][j] = w[indx]
    return True   

#Try to place word to the West South West
def tryPlaceWSW(grid,i,j,word):
       #remove white space
    w = word.replace(" ", "")
    #Is there room to the West South West
    if(len(grid) -i - len(w) < 0 or j+1 - len(w) < 0 ):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i+indx][j-indx] != w[indx] and grid[i+indx][j-indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i+indx][j-indx] = w[indx]
    return True

#Try to place word to the West    
def tryPlaceW(grid,i,j,word):
    #remove white space
    w = word.replace(" ", "")
    #Is there room to the West
    if(j+1 - len(w) < 0):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i][j-indx] != w[indx] and grid[i][j-indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i][j-indx] = w[indx]
    return True   
  
#Try to place word to the West North West    
def tryPlaceWNW(grid,i,j,word):
    #remove white space
    w = word.replace(" ", "")
    #Is there room to the West North West
    if(i+1 - len(w) < 0 or j+1 - len(w) < 0 ):
        return False
    #Will word conflict
    for indx in range(len(w)):
        if(grid[i-indx][j-indx] != w[indx] and grid[i-indx][j-indx] != '_'):
            return False
    #If here word did not conflict, so place word in grid
    for indx in range(len(w)):
        grid[i-indx][j-indx] = w[indx]
    return True


#retrieve at random one the the eight placement functions
def retrieveRandFunction(func_list):
    rand_indx = random.randint(0,len(func_list)-1)
    return func_list[ rand_indx]

#Places a word in the grid at a random poition and in a random direction
def placeWord(grid,func_list,word):
    #Potentially infinite loop, make sure grid is sufficiently large
    while(True):
        x_pos = random.randint(0,len(grid)-1)
        y_pos = random.randint(0,len(grid)-1)
        rand_func = retrieveRandFunction(func_list)
        if(rand_func(grid,x_pos,y_pos,word)):
            break
    return grid 


#Completes grid by replacing '_' by a random letter
def padGrid(grid):
    #Generate all Upper Case letters
    alphabet = list(string.ascii_uppercase)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == '_'):
                random.shuffle(alphabet)
                grid[i][j] = alphabet[0]
                

#List of 8 placement functions
#Functions are First Class Citizens in Python              
func_list = [tryPlaceN,tryPlaceENE,tryPlaceE,tryPlaceESE,tryPlaceS,tryPlaceWSW,
             tryPlaceW,tryPlaceWNW]

#Initialize grid
grid= [['_' for i in range(20)] for j in range(20)]

# ***** NB if the grid is too small for the the length or the word lengths
# ***** in the word list. The placement algorithm below might not terminate

for word in words:
    #Note this might not terminate
    placeWord(grid,func_list,word)
    print('***************************************')
    printGrid(grid)
    sleep(.5)
    
#Complete grid with random letters
padGrid(grid)

#Display final grid ready for a word search
printGrid(grid)
'''
Sample output 

I L K F D H D N E Z T I L B V A S P M O 
E V V I X E N D B J L Z B O N F F L Y F 
K S G O X Q I J O E F H P L O D U R S E 
H V R E H S A D P N N L Y R O A M Q A L 
L C S T N I C K Q S N Z L E R W U U L G 
T I H D E C C O P U Z E X C B K M C O N 
I P P I K J H H G W M O R N V W X A H I 
R M T C M R G O D V I R N A E D Z J C R 
A E N O C N N L E O L N O R C A I L I K 
S F E O F G E S C Y K A R P A N O E N S 
U O S D G C E Y O E A M T D L C Y S T S 
A U E E N T G Y R O N E H C P E I N S I 
L T R S K I H J A T D N P W E R O I K R 
C V P F A S E A T E C T O R R A F T G K 
A H T E M O C R I L O Y L E I I C A H B 
T O C R J N U T O T O P E A F Z R Y G J 
N B T I Z F P K N S K T O T A L X I I V 
A O F D K T I Q A I I Z O H A U G V E K 
S E I W A Y D B E M E J U N K U B K L P 
S O G P W M X T S R S E D R O O B X S O 
'''
 
