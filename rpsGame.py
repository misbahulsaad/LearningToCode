#this a simple Rock, Paper, Scissors game

import random, sys

print('ROCK, PAPER, SCISSORS')
#variables to keep track of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties' %(wins, losses, ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit')
    while True:
        playerMove = input()   #taking input of player move
        if playerMove == 'q':
            sys.exit() #quiting the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #making sure to take only r p s and q as input
        print('Type one of r, p, s or q.')

    if playerMove == 'r':
        print('Rock vs ...')
    elif playerMove == 'p':
        print('Paper vs ...')
    elif playerMove == 's':
        print('Scissors vs ...')
    

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie.')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or (playerMove == 'p' and computerMove == 'r') or (playerMove == 's' and computerMove == 'p'):
        print('You win')
        wins += 1
    elif (playerMove == 'r' and computerMove == 'p') or  (playerMove == 'p' and computerMove == 's') or (playerMove == 's' and computerMove == 'r'):
        print('You lose!')
        losses += 1