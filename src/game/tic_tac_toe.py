import random


class TicTacToe:
    def __init__(self) -> None:
        self.__board = [[' ' for _ in range(3)] for _ in range(3)]

        if random.randint(0, 1) == 1:
            self.__player_symbol, self.__computer_symbol = 'X', 'O'
        else:
            self.__player_symbol, self.__computer_symbol = 'O', 'X'

    def __print_board(self) -> None:
        for row in self.__board:
            print(" | ".join(row))
            print("-" * 9)

    def __check_winner(self, player: str) -> bool:
        for i in range(3):
            if (
                all(cell == player for cell in self.__board[i]) or
                all(row[i] == player for row in self.__board)
            ):
                return True

        if (
            all(self.__board[i][i] == player for i in range(3)) or
            all(self.__board[i][2 - i] == player for i in range(3))
        ):
            return True

        return False

    def __is_full(self) -> bool:
        return all(cell != ' ' for row in self.__board for cell in row)

    def __computer_move(self) -> tuple[int, int]:
        empty_cells = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.__board[row][col] == ' '
        ]
        return random.choice(empty_cells)

    def start_game(self) -> None:
        print("Welcome to Tic-Tac-Toe!")
        print(
            f"You play as {self.__player_symbol}, "
            f"the computer plays as {self.__computer_symbol}."
        )
        self.__print_board()
        while True:
            while True:
                try:
                    row = int(input("Enter row number (0-2): "))
                    col = int(input("Enter column number (0-2): "))
                    if self.__board[row][col] == ' ':
                        self.__board[row][col] = self.__player_symbol
                        break
                    else:
                        print("This cell is already occupied. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter numbers between 0 and 2.")
            self.__print_board()

            if self.__check_winner(self.__player_symbol):
                print("Congratulations, you won!")
                break
            if self.__is_full():
                print("It's a draw!")
                break

            row, col = self.__computer_move()
            self.__board[row][col] = self.__computer_symbol
            print(f"The computer made a move: row {row}, column {col}")
            self.__print_board()
            if self.__check_winner(self.__computer_symbol):
                print("Unfortunately, you lost. The computer won!")
                break
            if self.__is_full():
                print("It's a draw!")
                break
