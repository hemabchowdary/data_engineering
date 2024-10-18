<<<<<<< HEAD
import random
def display_board(board):
    print('   |   |   ')
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print('   |   |   ')
    print("-------------")
    print('   |   |   ')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print('   |   |   ')
    print("-------------")
    print('   |   |   ')
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print('   |   |   ')

def player_input():
    marker = ""
    
    while marker not in ['X','O']:
        marker = input("Player 1, Choose your marker( X or O): ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board,position):
    return board[position] == ' '

def player_choice(board):
    position = 0
    while position not in range(1,10) and not space_check(board,position):
        try:
            position = int(input("Choose your Next position (1-9): "))
        except ValueError:
            print("Please Enetr a valid Number b/w 1 and 9.")
    return position

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (
    (board[7] == board[8] == board[9] == marker) or 
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or  
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker) )   

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def replay():
    play_again = input("Do you want to play again? Enter Yes or No.").lower().startswith('y')
    return play_again

def play_game():
    print("Welcome to the Game of Tic Tac Toe!")
    while True:
        the_board = [' ']*10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(f"{turn} Will go First")

        play_game = input("Are you ready to play the game? Enter Yes or No: ").lower().startswith('y') # Yes or yes or YES or No or n

        game_on = play_game

        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                print("Player 1's Turn")
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("Congrats! Player 1 has Won the game!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                print("Player 2's Turn")
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("Congrats! Player 2 has Won the game!")
                    game_on = False
                
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break


play_game()
=======
import random
def display_board(board):
    print('   |   |   ')
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print('   |   |   ')
    print("-------------")
    print('   |   |   ')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print('   |   |   ')
    print("-------------")
    print('   |   |   ')
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print('   |   |   ')

def player_input():
    marker = ""
    
    while marker not in ['X','O']:
        marker = input("Player 1, Choose your marker( X or O): ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board,position):
    return board[position] == ' '

def player_choice(board):
    position = 0
    while position not in range(1,10) and not space_check(board,position):
        try:
            position = int(input("Choose your Next position (1-9): "))
        except ValueError:
            print("Please Enetr a valid Number b/w 1 and 9.")
    return position

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (
    (board[7] == board[8] == board[9] == marker) or 
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or  
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker) )   

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def replay():
    play_again = input("Do you want to play again? Enter Yes or No.").lower().startswith('y')
    return play_again

def play_game():
    print("Welcome to the Game of Tic Tac Toe!")
    while True:
        the_board = [' ']*10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(f"{turn} Will go First")

        play_game = input("Are you ready to play the game? Enter Yes or No: ").lower().startswith('y') # Yes or yes or YES or No or n

        game_on = play_game

        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                print("Player 1's Turn")
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("Congrats! Player 1 has Won the game!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                print("Player 2's Turn")
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("Congrats! Player 2 has Won the game!")
                    game_on = False
                
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break


play_game()
>>>>>>> 462a1859e0ae946ce42a5e4fb017030b6fe9da15
