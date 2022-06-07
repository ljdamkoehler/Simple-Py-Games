the_board = {
    '7': '(7)',
    '8': '(8)',
    '9': '(9)',
    '4': '(4)',
    '5': '(5)',
    '6': '(6)',
    '1': '(1)',
    '2': '(2)',
    '3': '(3)',
}

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('---+---+---')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---+---+---')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# print_board(the_board)... just testing to see if the board prints correctly

def game():
  """
  This function laysout the logic for this game.
  """
  turn = '_X_'

  count = 0

  win = False 

  while win == False:
    #Print the board and get the player's move
    print_board(the_board)
    print('It is your turn ' + turn + '. Which place would you like to go?')
    move = input()

    if the_board[move] != '_X_' and the_board[move] != '_O_':
      the_board[move] = turn
      count += 1
    else:
      print('That spot is already taken.\n\n Please select another place!')
    

    if count >= 5:
      if the_board['1'] == the_board['2'] == the_board['3']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['4'] == the_board['5'] == the_board['6']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['7'] == the_board['8'] == the_board['9']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['1'] == the_board['4'] == the_board['7']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['2'] == the_board['5'] == the_board['8']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['3'] == the_board['6'] == the_board['9']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['1'] == the_board['5'] == the_board['9']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break
      elif the_board['3'] == the_board['5'] == the_board['7']:
        win = True
        print('*** ' + turn + ' won! ***')
        print_board(the_board)
        break

    if count == 9:
      print('\nGAME OVER\n It was a tie!\n\n')

    if turn == '_X_':
      turn = '_O_'
    else:
      turn = '_X_'


game()
# print('Would you like to play again?')
# restart = input()