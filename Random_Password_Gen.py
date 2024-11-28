import random,string,zxcvbn as z

def pass_gen(length,lower_len,upper_len,special_len,num_len):
    password=[]
    for i in range(lower_len):
        password.append(random.choice(list(string.ascii_lowercase)))
        #print(password)
    for i in range(upper_len):
        password.append(random.choice(list(string.ascii_uppercase)))
        #print(password)
    for i in range(special_len):
        password.append(random.choice(list(string.punctuation)))
        #print(password)
    for i in range(num_len):
        password.append(random.choice(list(string.digits)))
        #print(password)
    for i in range(10000):
        random.shuffle(password)
    return password

length,col=int(input("Enter the length of the password you want?'\nGenerally recommended to use above 8:\n")),[]

with open('password_hash.txt','r') as file:
    hash_list = file.read()

while length<8:
    print('You are asking to be hacked.')
    length=int(input('Try Again\n'))
    
for i in range(10):
    lower_len,s=random.randint(1,length-3),''
    upper_len=random.randint(1,(length-lower_len-2))
    special_len=random.randint(1,(length-lower_len-upper_len-1))
    num_len=random.randint(1,(length-lower_len-upper_len-special_len))

    p=pass_gen(length,lower_len,upper_len,special_len,num_len)
    print('*'*90)
    for i,j in enumerate(p):
        #print(j,end='')
        s+=str(j)
    if s in col or str(hash(s)) in hash_list:
        continue
    else:
        col.append(s)
        result=z.zxcvbn(s)
        print(str(result['password'])+' is the password and it took '+ str(result['guesses'])+' guesses to break. Good Job, I guess.\nIt takes around '+ result.get('crack_times_display')['online_no_throttling_10_per_second']+ ' seconds with online no throttling 10 per second to break to crack this.\nMy score is '+str(result['score']))

index=int(input('Which one looks appeasing to you?\nRemeber to keep it in between 1 to 10\n'))
while index>10 or index<1:
    print('You are asking to be hacked.')
    index=int(input('Try Again\n'))
print(col[index-1] +" is your password. It's Hash will be stored for further security.")
with open('password_hash.txt','a') as file:
    file.write(str(hash(col[index-1]))+'\n')
