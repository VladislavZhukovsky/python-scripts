'''Blackjack game'''

from Blackjack.classes import BlackjackGame

def main():
    '''
    main function - Blackjack game
    '''
    game = BlackjackGame()
    game.invite_players()
    play_again = 'y'
    while play_again == 'y':
        game.play()
        play_again = input('Play again (y/n)?')

if __name__ == '__main__':
    main()
