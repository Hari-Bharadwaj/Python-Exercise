
def printf(board):
    print(board['tl']+' | '+board['tm']+' | '+board['tr'])
    print()
    print(board['ml']+' | '+board['mm']+' | '+board['mr'])
    print()
    print(board['dl']+' | '+board['dm']+' | '+board['dr'])
    print()

def sol_check(board):
    if board['tl']==board['tm']==board['tr'] and board['tl']!=' ':
        return board['tl']
    elif board['ml']==board['mm']==board['mr'] and board['ml']!=' ':
        return board['ml']
    elif board['dl']==board['dm']==board['dr'] and board['dl']!=' ':
        return board['dl']
    elif board['tl']==board['ml']==board['dl'] and board['tl']!=' ':
        return board['tl']
    elif board['tm']==board['mm']==board['dm'] and board['tm']!=' ':
        return board['tm']
    elif board['tr']==board['mr']==board['dr'] and board['tr']!=' ':
        return board['tr']
    elif board['tl']==board['mm']==board['dr'] and board['tl']!=' ':
        return board['tl']
    elif board['tr']==board['mm']==board['dl'] and board['dl']!=' ':
        return board['tr']
    else:
        return None
        

board={'tl':' ', 'tm':' ','tr':' ',
       'ml':' ', 'mm':' ','mr':' ',
       'dl':' ', 'dm':' ','dr':' '}

#print(board)

turn,move_set,balance = 'X',[],list(board.keys())
print('This is the board')
print('tl'+' | '+'tm'+' | '+'tr')
print()
print('ml'+' | '+'mm'+' | '+'mr')
print()
print('dl'+' | '+'dm'+' | '+'dr')
print()

for i in range(9):    
    for i in range(len(move_set)):
        if move_set[i] in balance:
            balance.remove(move_set[i])
    bal_string=' '.join(balance)
    move=str(input('Turn for '+turn+'. Move on which space? Your moves are: '+bal_string+' \n')).lower()
    while move not in balance:
        move=str(input('Try Again\n')).lower()
    while move in move_set:
        move=str(input('Already Played\n')).lower()
    move_set.append(move)
    #print(move)
    board[move]=turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'
    printf(board)
    win=str(sol_check(board))
    print('Winner is '+win)
    if win!='None':
        break
