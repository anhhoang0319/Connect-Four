"""

This file contains a main that will execute the game and allow user to play


"""
from connect_four import ConnectFour


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
