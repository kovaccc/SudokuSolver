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


def solveSudoku(board):
    empty_field = nextEmptyField(board)
    row_index = -1
    column_index = -1
    if empty_field is None:
        return True
    else:
        row_index = empty_field[0]
        column_index = empty_field[1]

    for number in range(1, 10):
        if isValidNumber(board, row_index, column_index, number):
            board[row_index][column_index] = number

            if solveSudoku(board):
                return True

            board[row_index][column_index] = 0
    return False


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

