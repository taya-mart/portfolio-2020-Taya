#Tic-Tac-Toe
#taya
#11-7-19

import random

#Global Constants
X="X"
O="O"
empty = "  "
num_squares = 9
tie= "tie"

#*working*
#instructions
def intro():
    """ display game instructions """
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.
        
        you will make your move known by entering a naumber, 1-9. The number
        will correspond to the board postition as illustrated:
        
                                         1  |  2  |  3
                                      --------------------
                                         4  |  5  |  6
                                      --------------------
                                         7  |  8  |  9
        
        Prepare yourself, human. The ultimate battle is about to begin. \n
        """)


#*working*
#new board
def new_board():
    board=[]
    for i in range(num_squares):
        board.append(empty)
    return board


#*working*
#display board
def display_board(board):
    """display game board on screen"""
    print(str.format("""
                                         {0}  |  {1}  |   {2}
                                       -------------------
                                         {3}  |  {4}  |   {5}
                                       -------------------
                                         {6}  |  {7}  |   {8}
    """,board[0], board[1], board[2],
         board[3], board[4], board[5],
         board[6], board[7], board[8]))


#*working*
#ask yes no
def ask_yes_no(question):
    """ask a question and give a one letter response back"""
    response=None
    while response not in ("y","n","no","yes"):
        response=input(question).lower()
    x=response[0]
    return x


#*working*
#ask numbers
def ask_number(question,low,high):
    response=None
    while response not in range(low,high):
         try:
            response=int(input(question))
         except:
            print("not a number ")
    return response


#*working*
#assign pieces
def assign_piece():
    go_first=ask_yes_no("do you require the first move? (y/n) : ")
    if go_first == "y":
        player=X
        comp=O
    else:
        comp=X
        player=O
    return comp, player


#*working*
#switch turns
def switch_turns(turn):
    if turn == X:
        return O
    else:
        return X


#*working*
#legal moves
def legal_moves(board):
    moves=[]
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)
    return moves


#*working*
#player turn
def player_turn(board,player):
    lm=legal_moves(board)
    move=None
    while move not in lm:
        move=ask_number("pick a number between 1 and 9 ",1,10)-1
        if move not in lm:
            print("that space is already taken")
    print("fine...")
    return move


#
#winner
def winner(board):
    """determine the game winner"""
    ways_to_win=((0,1,2),
                              (3,4,5),
                              (6,7,8),
                              (0,3,6),
                              (1,4,7),
                              (2,5,8),
                              (0,4,8),
                              (2,4,6))
    for row in ways_to_win:
        if board[row[0]] ==board[row[1]] == board[row[2]] !=empty:
            winner = board[row[0]]
            return winner
    if empty not in board:
        return tie
    return None


#
#computers turn
def comp_turn(board,comp,player):
    copy_board=board[:]
    best_moves_list=((0,8,2,6,1,3,5,7,4),(5,8,6,2,0,7,4,1,3),(6,2,0,4,8,3,1,7,5),(7,8,6,4,5,2,1,0,3))
    best_moves=random.choice(best_moves_list)
    print("I shall take square number", end=" ")
    #can computer win?
    for move in legal_moves(board):
        copy_board[move]=comp
        if winner(copy_board)==comp:
            print(move)
            return move
        copy_board[move]=empty
    #can player win?
    for move in legal_moves(board):
        copy_board[move]=player
        if winner(copy_board)==player:
            print(move)
            return move
        copy_board[move]=empty
    #best move possible?
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move

board=new_board()
board[0]=X
board[1]=O
x=comp_turn(board,O,X)
print(x)
board[x]=O
display_board(board)


#
#game
def game():
    turn=X
    intro()
    board=new_board()
    display_board(board)
    comp,player=assign_piece()
    while not winner(board):
        if turn==player:
            move=player_turn(board,player)
            board[move]=player
        else:
            move=comp_turn(board,comp,player)
            board[move]=comp
        display_board(board)
        turn=switch_turns(turn)
    if winner(board)==comp:
        print("YOU LOST :( ")
    elif winner(board)==player:
        print("YOU'VE WON! :D")
    elif winner(board)==tie:
        print("DRAW :I")


game()
