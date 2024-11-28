def isValidChessBoard(dic):
    key_list=list(dic.keys())
    pieces=['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for i in key_list:
        if i not in board_keys:
            return False
    item_list=list(dic.values())
    for i in item_list:
        #print(i)
        if i[0]=='w' or i[0]=='b':
            #print(i[0])
            piece=i[1:]
            if piece not in pieces:
                #print(piece)
                return False
        else:
            return False
    return True
                

board_keys=['1a','1b','1c','1d','1e','1f','1g','1h',
            '2a','2b','2c','2d','2e','2f','2g','2h',
            '3a','3b','3c','3d','3e','3f','3g','3h',
            '4a','4b','4c','4d','4e','4f','4g','4h',
            '5a','5b','5c','5d','5e','5f','5g','5h',
            '6a','6b','6c','6d','6e','6f','6g','6h',
            '7a','7b','7c','7d','7e','7f','7g','7h',
            '8a','8b','8c','8d','8e','8f','8g','8h',
            ]

input_dict={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
            '3e': 'wking'}

print(isValidChessBoard(input_dict))
