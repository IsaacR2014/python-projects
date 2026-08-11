import colorama
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

def run_game():
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1 = input("P1 Choose x|o: ").lower()
    if p1 == "x":
        p2 = "o"
        print("P2 you are o")
    elif p1 == "o":
        p2 = "x"
        print("P2 you are x")
    print_board()
    winner = None
    for turn in range(9):
        if turn % 2 == 0:
            while True:
                position = int(input("P1 Pick a position: "))
                if board[position - 1] in ["x", "o"]:
                    print("That spot is taken!")
                else:
                    board[position - 1] = p1
                    break
        else:
            while True:
                position = int(input("P2 Pick a position: "))
                if board[position - 1] in ["x", "o"]:
                    print("That spot is taken!")
                else:
                    board[position - 1] = p2
                    break
        print_board()
        winner = check_winner()
        if winner:
            print(f"{winner} wins!")
            break
    if not winner:
        print("It's a draw!")
    again = input("Play again? yes/no: ").lower()
    if again == "yes":
        run_game()
def check_winner():
    if board[0] == board[1] == board[2]:
        if board[0] in ["x", "o"]: return board[0]
    if board[3] == board[4] == board[5]:
        if board[3] in ["x", "o"]: return board[3]
    if board[6] == board[7] == board[8]:
        if board[6] in ["x", "o"]: return board[6]
    if board[0] == board[3] == board[6]:
        if board[0] in ["x", "o"]: return board[0]
    if board[1] == board[4] == board[7]:
        if board[1] in ["x", "o"]: return board[1]
    if board[2] == board[5] == board[8]:
        if board[2] in ["x", "o"]: return board[2]
    if board[0] == board[4] == board[8]:
        if board[0] in ["x", "o"]: return board[0]
    if board[2] == board[4] == board[6]:
        if board[2] in ["x", "o"]: return board[2]
    return None
run_game()
