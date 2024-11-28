def iron(spam):
    ans=''
    for i,j in enumerate(spam):
        ans+=str(j)
        #print(str(i)+' '+j+' '+ans)
        if i<(len(spam)-2):
            ans+=', '
        elif i == len(spam)-2:
            ans+=' and '
        else:
            ans+='.'
    return ans

spam = ['apples', 'bananas', 'tofu', 'cats']
#print(len(spam))
print(iron(spam))
