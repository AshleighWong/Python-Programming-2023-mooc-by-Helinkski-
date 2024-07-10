# Write your solution here
def row_correct(sudoku:list, row_no: int):
    row = sudoku[row_no]
    for i in range(1, 10):
        counter = row.count(i)
        if counter > 1:
            return False
    return True