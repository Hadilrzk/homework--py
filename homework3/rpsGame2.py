# First 3 wins
import random
choices= ['rock', 'paper',  'scissors']
print("Options are: Rock, Paper, Scissors")
playerscore = 0
computerscore = 0
round = 1
while playerscore < 3 and computerscore<3 :
    print("round",round)
    p = input('enter your choise:').replace(" ","").lower()
    if p not in choices:
        print('invalid choice, try again')
        continue
    c = random.choice(choices)
    print("compute chose:",c)
    if p == c :
        print('its a tie')
    elif (p=="rock" and c=="scissors") or (p=="scissors" and c=="paper") or (p=="paper" and c=="rock"):
        print("you win this round")  
        playerscore +=1
    else: 
        print("computer wins this round")    
        computerscore +=1
    round +=1
print('final score:')
print("you:",playerscore)
print('computer',computerscore)

if playerscore == 3 :
    print("you won the game")
else : print('computer won the game')    