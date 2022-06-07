print('...rock...')
print('...paper...')
print('...scissors...')

p1_wins = 0
p2_wins = 0

while p1_wins < 5 and p2_wins < 5:
    win = False

    while win == False:

        print('Enter player one\'s choice')
        p1 = input()

        print('NO CHEATING!!!\n\n' * 20)
        
        print('Enter player two\'s choice')
        p2 = input()

        if (p1 != 'rock' and p1 != 'paper' and p1 != 'scissors') or (p2 != 'rock' and p2 != 'paper' and p2 != 'scissors'):
            print('One or both of the players entered an invalid move! Please try again!')
        else:
            if p1 == p2:
                print('It was a tie! Try again!')
            else:
                win = True
                if p1 == 'rock' and p2 != 'paper':
                    p1_wins += 1
                    print('Player 1 wins the round!')
                elif p1 == 'paper' and p2 != 'scissors':
                    p1_wins += 1
                    print('Player 1 wins the round!')
                elif p1 == 'scissors' and p2 != 'rock':
                    p1_wins += 1
                    print('Player 1 wins the round!')
                else:
                    p2_wins += 1
                    print('Player 2 wins the round!')
        print('********************\n' * 3)

        print(f'Player 1 has a score of: {p1_wins} and Player 2 has a score of: {p2_wins}!')
        if p1_wins - 1 == 3 or p2_wins - 1 == 3:
            print('It is game point!')
        print('********************\n' * 3)
    
        if p1_wins == 5:
            print('Player 1 wins the match!')
        elif p2_wins == 5: 
            print('Player 2 wins the match!')