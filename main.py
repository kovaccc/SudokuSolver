import timeit


def printSudokuBoard(board):
    print("\n")
    for board_row in board:
        print(board_row)
    print("\n")


def nextEmptyField(board):
    for rowIndex in range(len(board)):
        for columnIndex in range(len(board[0])):
            if board[rowIndex][columnIndex] == 0:
                return rowIndex, columnIndex
    return None


def isValidNumber(board, row_index, column_index, number):
    for i in range(len(board[row_index])):
        if board[row_index][i] == number and column_index != i:
            return False

    for i in range(len(board)):
        if board[i][column_index] == number and row_index != i:
            return False

    for i in range(3):
        for j in range(3):
            if board[(row_index // 3) * 3 + i][
                (column_index // 3) * 3 + j] == number and i != row_index and j != column_index:
                return False
    return True


def solveSudoku(rootBoard):
    stack = [(-1, -1)]
    empty_field = nextEmptyField(rootBoard)

    while empty_field is not None:
        row_index = empty_field[0]
        column_index = empty_field[1]
        valid_number = rootBoard[row_index][column_index] + 1
        while valid_number < 10 and isValidNumber(rootBoard, row_index, column_index, valid_number) == False:
            valid_number = valid_number + 1

        if valid_number == 10:
            rootBoard[row_index][column_index] = 0
            empty_field = stack.pop()
            if empty_field == (-1, -1):
                return False
        else:
            rootBoard[row_index][column_index] = valid_number
            stack.append(empty_field)
            columnToAdd = 0 if empty_field[0] == 8 else empty_field[0] + 1
            rowToAdd = 0 if empty_field[1] == 8 else empty_field[1] + 1
            empty_field = nextEmptyField(rootBoard)
    return True


with open('Assignment 2 sudoku.txt') as sudokuFile:
    sudoku_file_lines = sudokuFile.readlines()
    sudokus = []
    board = []

    for line in sudoku_file_lines:
        if len(board) == 9:
            sudokus.append(board)
            board = []
        if line[0].isdigit() is False:
            continue
        else:
            boardRow = [int(i) for i in line[0:len(line) - 1]]
            board.append(boardRow)

    start = timeit.default_timer()
    for sudoku in sudokus:
        solveSudoku(sudoku)
        printSudokuBoard(sudoku)
    stop = timeit.default_timer()
    print('Sudoku solving time: ', stop - start)
