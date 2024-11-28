def collatz(number):
    if(number%2==0):
        number//=2
    else:
        number=3*number+1
    return number

try:
    number=input()
    while True:
        number=collatz(number)
        print(number)
        if number==1:
            break
except TypeError:
    print('Enter a number Dunce')
