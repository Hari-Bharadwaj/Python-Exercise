def check_type(word):
    if not word.isalpha():
        return word
    if word[0] in vowels_lower:
        word+='yay'
        return word
    elif word[0] in vowels_upper:
        word+='YAY'
        return word
    new_word=['']
    for i in range(len(word)):
        if word[i] in vowels_lower:
            if new_word==['']:
                new_world[0]=word
            new_word.append(word[i:]+'ay')
            return ''.join(new_word)
        elif word[i] in vowels_upper:
            if new_word==['']:
                new_world[0]=word
            new_word.insert(0,word[i:])
            new_word.append('AY')
            return ''.join(new_word)
        elif word[i].islower():
            if new_word[i-1].isupper():
                new_word[i-1]=new_word[i-1].lower()
                new_word.insert(0,word[i].upper())
                #print(word[i],new_word)
            else:
                new_word.insert(0,word[i])
        elif word[i].isupper():
            new_word.insert(0,word[i])
    nw=''.join(new_word)
    if nw[-1].islower():
        if not nw.endswith('ay'):
            nw+='ay'
            return nw
    if nw[-1].isupper():
        if not nw.endswith('AY'):
            nw+='AY'
            return nw
    return nw
        

#msg='My name is AL SWEIGART and I am 4,000 years old'
msg=input('Enter the English message to translate into Pig Latin:\n')
vowels_lower,vowels_upper=['a','e','i','o','u'],['A','E','I','O','U']
sen_list=msg.split()

for i in sen_list:
    print(check_type(i),end=' ')
