# Best of 3
import random
choices= ['rock', 'paper', 'scissors']
print("Options are: Rock, Paper, Scissors")
playerScore = 0
computeScore =0
for round in range(1,4):
    print('Round',round)
    p = input('enter your choise:').replace(" ","").lower()
    if p not in choices:
        print ('invalid choise,try againe')
        continue
    computer = random.choice(choices)
    print('computer chose:',computer)

    if p == computer:
        print('it is a tie')
    elif (p=="rock" and computer=="scissors") or (p=="scissors" and computer=="paper") or (p=="paper" and computer=="rock"):
        print('you win the round')
        playerScore += 1    
    else:
        print('computer wins the round')
        computeScore += 1
print('final score')
print("you:",playerScore)
print("computer:",computeScore)

if playerScore> computeScore:
    print("you win the game'best of three'")
elif computeScore > playerScore:
    print('computer won the game')
else: print('its a draw')

