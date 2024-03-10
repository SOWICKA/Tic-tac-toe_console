import random

def print_board(board):
    print("    A   B   C")
    print("  ┌───┬───┬───┐")
    for i, row in enumerate(board):
        print(f"{i+1} | {' | '.join(row)} |")
        if i < 2:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def get_move(player, board):
    while True:
        try:
            move = input(f"{player}, podaj współrzędne (np. A1, B3): ").upper()
            if len(move) == 2 and move[0] in 'ABC' and move[1] in '123':
                col, row = ord(move[0]) - 65, int(move[1]) - 1
                if board[row][col] == " ":
                    return row, col
                else:
                    print("To pole jest już zajęte. Wybierz inne.")
            else:
                print("Nieprawidłowy ruch. Spróbuj ponownie.")
        except ValueError:
            print("Nieprawidłowy ruch. Spróbuj ponownie.")

def computer_move_easy(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def computer_move_medium(board, player_symbol):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player_symbol
                if check_win(board):
                    return row, col
                board[row][col] = " "

    opponent_symbol = "X" if player_symbol == "O" else "O"
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = opponent_symbol
                if check_win(board):
                    return row, col
                board[row][col] = " "

    return computer_move_easy(board)

def computer_move_hard(board, player_symbol):

    
    return computer_move_medium(board, player_symbol)

def computer_move(board, player_symbol, difficulty):
    if difficulty == 'łatwy':
        return computer_move_easy(board)
    elif difficulty == 'średni':
        return computer_move_medium(board, player_symbol)
    else:  # trudny
        return computer_move_hard(board, player_symbol)

def two_player_game():
    player1 = input("Podaj imię pierwszego gracza: ")
    player2 = input("Podaj imię drugiego gracza: ")
    current_player, symbol = player1, "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for turn in range(9):
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = symbol
        if check_win(board):
            print_board(board)
            print(f"Wygrana! Gratulacje, {current_player}!")
            return
        current_player, symbol = (player2, "O") if current_player == player1 else (player1, "X")
    print_board(board)
    print("Remis!")

def computer_game(difficulty, player_symbol):
    player = input("Podaj swoje imię: ")
    computer_symbol = "O" if player_symbol == "X" else "X"
    current_player = player
    board = [[" " for _ in range(3)] for _ in range(3)]
    for turn in range(9):
        print_board(board)
        if current_player == player:
            row, col = get_move(current_player, board)
            board[row][col] = player_symbol
            if check_win(board):
                print_board(board)
                print(f"Wygrana! Gratulacje, {current_player}!")
                return
        else:
            row, col = computer_move(board, computer_symbol, difficulty)
            board[row][col] = computer_symbol
            print("Ruch komputera:")
            if check_win(board):
                print_board(board)
                print("Komputer wygrał!")
                return
        current_player = computer_symbol if current_player == player else player
    print_board(board)
    print("Remis!")

def game_rules():
    print("Witaj w grze Kółko i Krzyżyk!")
    print("Gra polega na zajmowaniu pól na planszy 3x3.")
    print("Plansza jest oznaczona literami A, B, C dla kolumn i cyframi 1, 2, 3 dla wierszy.")
    print("Gracze na zmianę wybierają pole, na którym chcą postawić swój znak.")
    print("Pierwszy gracz używa znaku 'X', a drugi gracz używa znaku 'O'.")
    print("Celem gry jest ułożenie trzech swoich znaków w rzędzie, kolumnie lub na przekątnej.")
    print("Plansza wygląda następująco:")
    print_board([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
    print("Przykład poprawnego ruchu: 'A1' lub 'C2'.")
    print("Powodzenia!\n")

if __name__ == "__main__":
    game_rules()
    while True:
        print("Wybierz tryb gry:")
        print("1 - gra dwuosobowa")
        print("2 - gra z komputerem")
        choice = input("Wpisz 1 lub 2: ")
        if choice == "1":
            two_player_game()
        elif choice == "2":
            print("Wybierz poziom trudności:")
            print("1 - łatwy")
            print("2 - średni")
            print("3 - trudny")
            difficulty_choice = input("Wpisz 1, 2 lub 3: ")
            difficulty = 'łatwy' if difficulty_choice == '1' else 'średni' if difficulty_choice == '2' else 'trudny'

            player_symbol = ""
            while player_symbol not in ["X", "O"]:
                player_symbol = input("Wybierz swój symbol (X/O): ").upper()
                if player_symbol not in ["X", "O"]:
                    print("Nieprawidłowy wybór. Wybierz 'X' lub 'O'.")

            computer_game(difficulty, player_symbol)
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
        if input("Czy chcesz zagrać ponownie? (tak/nie): ").lower() != "tak":
            break
