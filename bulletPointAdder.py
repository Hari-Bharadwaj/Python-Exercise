import pyperclip


mylist=pyperclip.paste()

# TODO: Separate lines and add stars.

#print(mylist)

pyperclip.copy(mylist)

comp=mylist.split('\r\n')

for i in range(len(comp)):
    print('* '+comp[i])
    comp[i]='* '+comp[i]

mylist='\r\n'.join(comp)
pyperclip.copy(mylist)
print(mylist)
