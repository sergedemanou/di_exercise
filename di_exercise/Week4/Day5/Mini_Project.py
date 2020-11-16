                     # Mini-Project - Tic Tac Toe
# Create a TicTacToe game in python, where two users can play together.
# Here Are The Rules:
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# Hint
# To do this project, you basically need to program four functions: * display_board() – To display Tic Tac Toe board (GUI). * player_input(player) – To get input position from the player. * check_win() – To check winner of the game. * play() – More like the main function, which calls above function for gameplay.
#
# Note: The 4 functions above are just an example idea. You can implement many more helper functions or choose a completely different design if you want.
#
# Tips : Consider The Following:
# What actions will need to happen every turn to make this program work?
# With the question above in mind, think about how to break up your code into smaller pieces (functions)
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

tableau =[['1','|','2','|','3'],['--','--','--'],['4','|','5','|','6'],['--','--','--'],['7','|','8','|','9']]
liste_dispo = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
def display_board():
    for i in tableau:
        print(''.join(i))

def player_input(player):
    player = input("Quel joueur êtes vous?. Entrez 'X' pour le joueur X et 'O' pour le joueur O :" )
    position = input("Dans quelle case voulez vous jouer?")
    while int(position) not in liste_dispo :
    # if int(position) in liste_dispo :
        position = input("entrer un autre numero : ")

    else:
        for i in tableau :
            try:
                i_pos = i.index(position)
                i[i_pos] = player
            except ValueError:
                continue
        print(tableau)
        display_board()
        liste_dispo.remove(int(position))

# display_board()
# player_input()

def play():
    display_board()
    player1 = 'X'
    player2= 'O'
    turn =0
    while turn<9:
        if turn%2==0 :
            player_input(player1)
        else:
            player_input(player2)
        turn += 1
play()




