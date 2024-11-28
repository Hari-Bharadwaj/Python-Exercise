import random
ans,req,c=random.randint(1,20),0,0
print('I am thinking of a number between 1 and 20.')
while req!=ans:
    req,c=int(input('Take a guess\n')),c+1
    if req>ans:
        print('Your guess is too high.')
    elif req<ans:
        print('Your guess is too low.')
    else:
        break
print('Good job! You guessed my number in '+str(c)+' guesses!')
