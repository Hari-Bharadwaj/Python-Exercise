'''
It's a joke. Get it? 'Enter' your name?
'''
name,c,num='',0,0
while name!='your name':
    name=input('Enter your name:\n')
    if name=='yo mama':
        print('You are confused. But on the right track.')
        continue
    num=int(input('Enter your age:\n'))
    if num:
        print('Are you really '+str(num)+' old?')
    if c==4:
        break
print('Hi '+name+". I'm dad")
