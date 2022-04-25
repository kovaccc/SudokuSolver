def printSudokuBoard(board):
    for board_row in board:
        print(board_row)


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

    for sudoku in sudokus:
        printSudokuBoard(sudoku)
        print("\n")
