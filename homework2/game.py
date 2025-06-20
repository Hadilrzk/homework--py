p1=input('the first player choose: rock,paper,scissors:')
p2=input('the second player choose: rock,paper,scissors:')
if p1 == p2:
    print('try again')
elif (p1=='rock' and p2=='scissors') or (p1=='paper' and p2=='rock') or (p1=='scissors'and p2=='paper'):
    print('player 1 is win')
elif (p2=='rock' and p1=='scissors') or (p2=='paper' and p1=='rock') or (p2=='scissors'and p1=='paper'):
    print('player 2 is win')
