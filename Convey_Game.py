
import random as r, copy

def shift(Convey,height,width):
    nextcopy=copy.deepcopy(Convey)
    for i in range(height):
        for j in range(width):
            lx,ly,ux,uy,ne=(i-1)%width,(j-1)%height,(i+1)%width,(j+1)%height,0
            if Convey[lx][ly]=='#':
                ne+=1
            if Convey[lx][j]=='#':
                ne+=1
            if Convey[lx][uy]=='#':
                ne+=1
            if Convey[i][ly]=='#':
                ne+=1
            if Convey[i][uy]=='#':
                ne+=1
            if Convey[ux][ly]=='#':
                ne+=1
            if Convey[ux][j]=='#':
                ne+=1
            if Convey[ux][uy]=='#':
                ne+=1
            if (ne == 2 or ne == 3) and Convey[i][j]=='#':
                nextcopy[i][j]='#'
            else:
                nextcopy[i][j]='-'
            if Convey[i][j]=='0' and ne==3:
                nextcopy[i][j]='#'
    return nextcopy


        
    

width,height=6,6
Convey=[]

for i in range(height):
    column=[]
    for j in range(width):
        if r.randint(0,1) == 1:
            column.append('#')
        else:
            column.append('-')
    Convey.append(column)


for i,j in enumerate(Convey):
    print(j)

print('---------------------------')
nextcopy=copy.deepcopy(Convey)
for i in range(4):
    nextcopy=shift(nextcopy,height,width)
    print('This is %s shift'%i)
    for j,k in enumerate(nextcopy):
        print(k)
    print('---------------------------')
    
        
        
        
