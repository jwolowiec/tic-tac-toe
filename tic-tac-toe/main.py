fields = {}
player_char = "O"
player_round = True
type_of_player = "Circle"
rounds_count = 0
board = []
field_number = 1

for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
        field_number += 1
    board.append(row)


def draw():
    draw_board = ""
    print("-------------")
    for draw_row in range(3):
        draw_board += "| "
        for draw_col in range(3):
            draw_board += str(board[draw_row][draw_col]) + " | "
        draw_board += "\n-------------\n"
    print(draw_board)


def is_occupied(check_row, check_col):
    if check_row < 1 and check_col < 1 or check_row > 3 and check_col > 3:
        print("Wrong field number")
        return False
    elif board[check_row - 1][check_col - 1] == "X" or board[check_row - 1][check_col - 1] == "O":
        print("The field is already occupied")
        return False
    else:
        return True


def is_win():
    for win_row_r in range(3):
        chars_row_number = 0
        for win_col_r in range(3):
            if board[win_row_r][win_col_r] == player_char:
                chars_row_number += 1
        if chars_row_number == 3:
            print(f"{type_of_player} is winner")
            return True

    for win_row_c in range(3):
        chars_col_number = 0
        for win_col_c in range(3):
            if board[win_col_c][win_row_c] == player_char:
                chars_col_number += 1
        if chars_col_number == 3:
            print(f"{type_of_player} is winner")
            return True

    chars_number_diagonal_start = 0
    for win_diagonal_start in range(3):
        if board[win_diagonal_start][win_diagonal_start] == player_char:
            chars_number_diagonal_start += 1
        if chars_number_diagonal_start == 3:
            print(f"{type_of_player} is winner")
            return True

    chars_number_diagonal_end = 0
    for win_diagonal_end in range(3):
        if board[win_diagonal_end][len(board) - 1 - win_diagonal_end] == player_char:
            chars_number_diagonal_end += 1
        if chars_number_diagonal_end == 3:
            print(f"{type_of_player} is winner")
            return True


while True:
    draw()

    if player_round:
        type_of_player = "Circle"
        player_char = "O"
    elif not player_round:
        type_of_player = "Cross"
        player_char = "X"

    print(f"{type_of_player} round")
    movement_row = int(input("Enter row number: "))
    movement_col = int(input("Enter column number: "))

    if is_occupied(movement_row, movement_col):
        board[movement_row - 1][movement_col - 1] = player_char
        if is_win():
            draw()
            break
        player_round = not player_round
        rounds_count += 1

    if rounds_count == 9:
        draw()
        print("End of the game. Draw")
        break
