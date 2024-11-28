import time,sys
space,front=0,True
try:
    while True:
        print(' '*space+'********')
        if front and space<4:
            space+=1
        elif space==4:
            front=False
            space-=1
        elif front!=True and space==0:
            front=True
            space+=1
        elif front!=True and space<4:
            space-=1
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
