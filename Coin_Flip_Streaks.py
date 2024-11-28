import random

def streak_count(Toss):
    c, s, tc, hs = 0, '', 0, []
    for i, j in enumerate(Toss):
        if j == 'H':
            if c == 0:
                c += 1
                s = 'H'
            elif c != 0 and s == 'H':
                c += 1
            elif c != 0 and s != 'H':
                c = 0
                s = 'H'
        else:
            if c == 0:
                c += 1
                s = 'T'
            elif c != 0 and s == 'T':
                c += 1
            elif c != 0 and s != 'T':
                c = 0
                s = 'T'
        if c == 6:
            tc += 1
            c = 0
            hs.append(s)
    return tc

Toss = []
for i in range(100):
    if random.randint(0, 1) == 1:
        Toss.append('H')
    else:
        Toss.append('T')
final_count=0
for i in range(10001):
    '''print('Attempt number '+ str(i+1))
    print(streak_count(Toss))'''
    Toss = []
    for i in range(100):
        if random.randint(0, 1) == 1:
            Toss.append('H')
        else:
            Toss.append('T')
    final_count+=streak_count(Toss)
print(final_count)
