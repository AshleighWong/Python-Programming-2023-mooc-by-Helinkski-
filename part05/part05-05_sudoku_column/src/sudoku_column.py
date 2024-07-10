# Write your solution here
def column_correct(sudoku:list, column_no:int):
    numbers =[]
    for row in sudoku:
        col = row[column_no]
        if col > 0 and col in numbers:
            return False
        numbers.append(col)
    return True