"""


This file contains a Class name ConnectFour that create Connect Four game
where players try to get four of their pieces in a row, a column, or a
diagonal.


"""


class ConnectFour:

    def __init__(self):
        self.board = [[" " for i in range(7)] for j in range(6)]
        self.turns = "X"
        self.row = 6
        self.col = 0
        self.tracking_list = list()

    def print_board(self):
        """
        Print the board which contains pieces of each player after their turn
        :return: the board
        """
        board = ""
        for row in self.board:
            for col in row:
                board += "|" + str(col)
            board += "|\n"
            board += "---------------" + "\n"
        return board

    def add_piece(self, column):
        """
        Place the piece into the column that is specifying
        :param column: int | Place the piece into this column
        :return: row, column | location of the piece in the board
        """
        self.col = column

        column = column - 1
        if type(column) != int:
            raise ValueError("Not a valid input")
        if self.row == 0:
            raise ValueError("The column is already full!")
        if column < 0 or column > 7:
            raise ValueError("Outside of playing area")
        if self.is_game_over(self.board):
            raise ValueError("The game is over")
        try:
            if 0 <= column <= 6:
                for row in range(5, -1, -1):
                    if self.board[row][column] == " ":
                        self.tracking_list.append([row, column])
                        return row, column

        except ValueError as error:
            print(error)

    def mark_board(self, row, col):
        """
        Mark the piece that is specifying to player X or O
        and switch turn
        :param row: int | in which row the piece is marked
        :param col: int | in which column the piece is marked
        :return: str | Marked X or O on the board
        """
        self.row = row
        self.col = col

        if self.turns == "X":
            self.board[row][col] = "X"
            self.turns = "O"
        else:
            self.board[row][col] = "O"
            self.turns = "X"
        return self.board

    def is_full(self):
        nums = 0
        for element in self.board[0]:
            if element == "O" or element == "X":
                nums += 1

        if nums == 7:
            return True
        else:
            return False

    def is_game_over(self, board):
        """
        Decide when and how the game is over with a winner
        :param board: str | the location of pieces in the board
        :return: boolean | True if 4 pieces are on a row, a column, or a
        diagonal, if condition is not met, return False
        """
        # Check for starting position of diagonal
        # going up and to the right
        player = self.turns
        for row in range(3, 6):
            for col in range(0, 4):
                if board[row][col] == player and \
                        board[row - 1][col + 1] == player and \
                        board[row - 2][col + 2] == player and \
                        board[row - 3][col + 3] == player:
                    return True

        # Check for starting position of diagonal
        # going down and to the right
        for row in range(0, 3):
            for col in range(0, 4):
                if board[row][col] == player and \
                        board[row + 1][col + 1] == player and \
                        board[row + 2][col + 2] == player and \
                        board[row + 3][col + 3] == player:
                    return True

        # Check for starting position of horizontal
        for row in range(0, 6):
            for col in range(0, 4):
                if board[row][col] == player and \
                        board[row][col + 1] == player and \
                        board[row][col + 2] == player and \
                        board[row][col + 3] == player:
                    return True

        # Check for starting position of vertical
        for row in range(0, 3):
            for col in range(0, 7):
                if board[row][col] == player and \
                        board[row + 1][col] == player and \
                        board[row + 2][col] == player and \
                        board[row + 3][col] == player:
                    return True

        if self.is_full():
            return True
        return False

    def get_winner(self):
        """
        Decide the winner
        :return: str | who is the winner, if the board is full and there is no
        winner, the game ends with a tie

        """
        while self.is_game_over(self.board):
            if self.is_full():
                print("Game Over")
                print("The game ends in a tie")
                return None
            print("Game Over")
            print("Winner is " + str(self.turns))
            return

    def undo(self):
        if len(self.tracking_list) == 0:
            raise ValueError("Cannot undo!")
        row, col = self.tracking_list.pop()
        self.board[row][col] = " "

    def __str__(self):
        board = self.print_board()
        return board


def main():
    b = ConnectFour()
    print(b)
    while True:
        options = list_options()
        command = input(options)
        if command == "U":
            b.undo()
            print(b.print_board())
            continue

        if command == "Q":
            break
        else:
            column = int(command)
            row, col = b.add_piece(column)
            board = b.mark_board(row, col)
            print(b.print_board())
            if b.is_game_over(board):
                b.get_winner()
                break


def list_options():
    options = "Choose an option:\n"
    options += "Q - Quit \n"
    options += "U - Undo \n"
    options += "Or pick a column (1 - 7): "
    return options


if __name__ == "__main__":

    main()
