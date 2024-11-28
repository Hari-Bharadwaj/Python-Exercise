import random as r

print('ROCK, PAPER, SCISSORS')
hand,bot='',''
w,l,t=0,0,0
while hand!='q':
    print('%s Wins, %s Losses, %s Ties'%(w,l,t))
    hand,bot=input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n'),r.choice(['p','s','r'])
    if hand=='p':
        print('PAPER versus...')
    elif hand=='s':
        print('SCISSORS versus...')
    elif hand=='r':
        print('ROCK versus...')
    else:
        continue
    
    if bot=='p':
        print('PAPER')
    elif bot=='s':
        print('SCISSORS')
    elif bot=='r':
        print('ROCKs')

    if hand==bot:
        print('It is a tie!')
        t+=1
    elif hand=='r' and bot =='s':
        print('You Win')
        w+=1
    elif hand=='r' and bot == 'p':
        print('You Lose')
        l+=1
    elif hand=='p' and bot =='r':
        print('You Win')
        w+=1
    elif hand=='p' and bot == 's':
        print('You Lose')
        l+=1
    elif hand=='s' and bot =='p':
        print('You Win')
        w+=1
    elif hand=='s' and bot == 'r':
        print('You Lose')
        l+=1
    




'''
for i in range(100):
    print(r.choice(['p1','s','r']))
'''
