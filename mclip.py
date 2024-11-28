#! python3
import sys, pyperclip

Text_prompt = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv)<2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyword=sys.argv[1]

if keyword in Text_prompt:
    pyperclip.copy(Text_prompt[keyword])
    print(Text_prompt.get(keyword))
else:
    print('No keyword assigned')
    
    
