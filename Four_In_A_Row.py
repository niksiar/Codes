"""
Input:

In the first line of input, the number n is given, which is the number of all moves in the game. These moves start
with the red player (r). That is, if 7 moves were given, it means that the red player had 4 moves and the yellow
player (y) had 3 moves. The houses are numbered from left to right with numbers from one to seven. In the next input
line, n is given as a number between 1 and 7, which is the house number in which the player with the turn throws his
piece (the dosing game screen always has 6 rows of 7 columns). This program guarantees that a house number that can
not be played in will never be given as input.

At the output of the program, you must print the name of the winning player and the final board of the game.

Important note:

In implementing this question, these three functions must be used:
A function that takes as input the 2D list of the game screen and prints it similar to what is given in the sample
tests
The function that takes as input the 2D list of the game screen and the number of columns considered by the
player and the name of the color of the player's piece. And record the player's desired move on the game page and
return to the new game page
A function that takes the final and complete page of the game as the input of the 2D list
and determines and returns the color of the winning player by examining the page (of course, determining the winner
based on the number of moves performed is not acceptable)

"""

fn = 7
num = 6

FINAL_BOARD = []
#


def game_board(number):
    board = []
    for y in range(number):
        u = []
        for x in range(fn):
            u.append(0)
        board.append(u)
    return board

no_move = int(input())
move = input().split()
game_board(num)
#
moves_dic = dict()

def moves(board, move):
    nm = 0
    t = 1
    j = 1
    for n in move:
        nm += 1
        if int(n) in moves_dic:
            moves_dic[int(n)] += 1
        else:
            moves_dic[int(n)] = 1
        if int(nm) % 2 == 0:
            # print('yellow')
            if board[num - 1][int(n) - 1] == 0:

                board[num - 1][int(n) - 1] = 'y'
            else:
                board[num - (moves_dic[int(n)])][int(n) - 1] = 'y'
            t = t + 1

        elif int(nm) % 2 == 1:
            # print('red')
            if board[num - 1][int(n) - 1] == 0:

                board[num - 1][int(n) - 1] = 'r'
            else:
                board[num - (moves_dic[int(n)])][int(n) - 1] = 'r'
            j = j + 1

        if nm == no_move:  # to see every single move, remove the if statement
            # print(f"move number {nm}")  # to see the number of move, remove the first {#}
            for x in board:
                FINAL_BOARD.append(x)
                """for f in x:
                    print(f, end=' ')
                print()"""
    return board




def winner_finder(fb):
    # ofoghi
    for n in range(fn - 3):
        for rows in fb:
            reds = 0
            yellows = 0
            for u in range(4):
                try:
                    if rows[n + u] == 'r':
                        reds += 1

                    elif rows[n + u] == 'y':
                        yellows += 1
                except:
                    continue
            # print('yellows:',yellows)
            # print('reds:', reds)
            if yellows == 4:
                Winner = 'yellow'
                return Winner
            elif reds == 4:
                Winner = 'red'
                return Winner

    # amudi
    for o in range(7):
        reds = 0
        yellows = 0
        for t in range(7):
            # print(fb[t][o])
            try:
                if fb[t][o] == 'r':
                    reds += 1
                elif fb[t][o] == 'y':
                    yellows += 1
            except:
                continue
            # print('yellows:',yellows)
            # print('reds:', reds)
            if yellows == 4:
                Winner = 'yellow'
                return Winner
            elif reds == 4:
                Winner = 'red'
                return Winner

    # orib az chap be rast
    for k in reversed(range(4)):
        for n in range(7):
            reds = 0
            yellows = 0
            for u in reversed(range(k, k + 4)):
                # print('n,u',u,n)
                try:
                    if fb[u][n] == 'r':
                        reds += 1
                    elif fb[u][n] == 'y':
                        yellows += 1
                    # print('yellows:',yellows)
                    # print('reds:', reds)
                    if yellows == 4:
                        Winner = 'yellow'
                        return Winner
                    elif reds == 4:
                        Winner = 'red'
                        return Winner
                    n = n + 1
                except:
                    continue
    #

    # orib az rast be chap
    for k in reversed(range(4)):
        for n in reversed(range(7)):
            reds = 0
            yellows = 0
            for u in reversed(range(k, k + 4)):
                if n >= 0:
                    # print('u,n', u, n)
                    try:
                        if fb[u][n] == 'r':
                            reds += 1
                        elif fb[u][n] == 'y':
                            yellows += 1
                        # print('yellows:',yellows)
                        # print('reds:', reds)
                        if yellows == 4:
                            Winner = "yellow"
                            return Winner
                        elif reds == 4:
                            Winner = 'red'
                            return Winner
                        n = n - 1
                    except:
                        continue


if (winner_finder(moves(game_board(num), move))) == 'red':
    print('Winner = r')
else:
    print('Winner = y')

for X in (FINAL_BOARD):
    for T in X:
        print(T, end=' ')
    print()
