'''
Made by Christopher Geiger on 10/19/2016
Created for educational purposes
'''



# Welcomes user
# Get user input
# Calculate computer's throw
# Resolve situation (who wins, is there a tie)
# Loop

import random

def welcome():
    print('Welcome to RPS!')
    print('Please choose a move:')
    print('Rock - 1\nPaper - 2\nScissors - 3')

def getCompThrow():
    print("Getting the computer's throw...")
    compThrow = random.randint(1,3)
    print("The computer threw a ", end='')
    
    if(compThrow == 1):
        print('rock!')
    elif(compThrow == 2):
        print('paper!')
    else:
        print('scissor!')
        
    return compThrow

def resolve(uThrow, cThrow):
    if(uThrow == cThrow):
        print('There has been a tie!')
    elif(uThrow == 1 and cThrow == 2):
        print('You lost!')
    elif(uThrow == 2 and cThrow == 3):
        print('You lost!')
    elif(uThrow == 3 and cThrow == 1):
        print('You lost!')
    else:
        print('You won!')

def clear():
    print('\n' * 100)
    
while True:
    clear()
    welcome()
    usrThrow = int(input())
    resolve(usrThrow, getCompThrow())
    print('Play again? Y/N')
    if(input().lower() != 'y'):
        break
