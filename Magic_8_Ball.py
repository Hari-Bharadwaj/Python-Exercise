import random
messages=['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

ans=random.choice(messages)
print('The number is %s' %messages.index(ans)+' and the message is: '+ans)
