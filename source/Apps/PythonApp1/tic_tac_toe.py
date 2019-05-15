lines = ['   |   |   ', ' {} | {} | {} ', '---|---|---']

def get_player_symbol(player):
    symbol = input('Player {}, enter your symbol: '.format(player + 1))
    players[player] = symbol

def printField():
    print(lines[0])
    print(lines[1].format(field[6], field[7], field[8]))
    print(lines[0])
    print(lines[2])
    print(lines[0])
    print(lines[1].format(field[3], field[4], field[5]))
    print(lines[0])
    print(lines[2])
    print(lines[0])
    print(lines[1].format(field[0], field[1], field[2]))
    print(lines[0])

def make_move(player):
    move_s = input('Player {}, make a move: '.format(player + 1))
    move = int(move_s)
    field[move - 1] = players[player]

import os
clear = lambda: os.system('cls')

def is_winning_line(a,b,c):
    return (not ' ' in [field[a], field[b], field[c]]) and (field[a] == field[b] == field[c])

def end():
    return is_winning_line(0,1,2) or is_winning_line(3,4,5) or is_winning_line(6,7,8) or is_winning_line(0,3,6) or is_winning_line(1,4,7) or is_winning_line(2,5,8) or is_winning_line(0,4,8) or is_winning_line(2,4,6)

while(True):
    clear()
    field = [' '] * 9
    players = ['', '']
    get_player_symbol(0)
    get_player_symbol(1)
    clear()
    currentPlayerMove = -1
    moves = 0
    while(True):
        print(f'Player 1: {players[0]}')
        print(f'Player 2: {players[1]}')
        printField()
        currentPlayerMove = (currentPlayerMove + 1) % 2
        if moves == 9:
            print("It's a draw!")
            break;
        if end():
            print("Player {}, you've won!".format(currentPlayerMove + 1))
            break;
        make_move(currentPlayerMove)
        moves += 1
        clear()
    startNewGame = input("Play again (y/n)? ")
    if startNewGame == 'n':
        break