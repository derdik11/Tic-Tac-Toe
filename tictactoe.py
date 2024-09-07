
import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

wins = 0

loses = 0


def board_show():
    for row in board:
        print("|".join(row))
        print("_" * 5)


def play(player):
    try:

        row = int(input('Choose row '))
        col = int(input('Choose column '))

        if board[row][col] == ' ':
            board[row][col] = player

        else:
            print('This place is taken, try another one!')
            play(player)

    except (IndexError, ValueError):
        print('Not right Value')
        play(player)

        
def check_win(board, player):
    
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True

    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True

    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

def computer_move(comp_player):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = comp_player
        print(f"Computer plays at row {row}, column {col}.")

def play_game():
    global board, wins, loses
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    hum_player = str.lower(input('Choose your side(x or o): '))
    
    if hum_player == 'x':

        comp_player = 'o'

    elif hum_player == 'o':

        comp_player = 'x'

    turns = 0
    
    current_player = 'x'

    while turns < 9:  

        board_show()
            
        if current_player == hum_player:
            print(f"Player {current_player}'s turn.")
            play(hum_player)
        else:
            computer_move(comp_player)
            
        if check_win(board, current_player):
            board_show()

            if current_player == hum_player:
                print('Human wins!')
                wins += 1
            else:
                print('Computer wins!')
                loses += 1
            return
            
        if current_player == 'x':

            current_player = 'o'

        else:

            current_player = 'x'
            
        turns += 1
            
    board_show()
    print("It's a tie!")



def main():
    global wins, loses

    print('Hello to the Tic Tac Toe game\nYou can play it with your friends\nJust pick your side (x or o)')

    while True:

        play_game()

        print(f'Score: \n      Wins: {wins} \n      Loses: {loses}')

        print('Do you want restart game? (y/n)')
        answer = str.lower(input('Write y or n: '))

        if answer != 'y':
            print(f'Thank you for playing my game!\n      Human wins: {wins}\n      Human loses: {loses}')
            break

main()