# Write your solution here

def row_correct(sudoku: list):
    for i in range(9):
        numbers = []
        row = sudoku[i]
        for item in row:
            if item > 0 and item in numbers:
                return False
            numbers.append(item)
    return True


def column_correct(sudoku:list):
    numbers = []
    col = 0
    for row in range(9):
        item = sudoku[row][col]
        if item > 0 and item in numbers:
            return False
        numbers.append(item)
    numbers = []
    col+=1
    return True
            
            
        
 
def block_correct(sudoku: list):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            numbers = []
            for i in range(3):
                for j in range(3):
                    item = sudoku[row + i][col + j]
                    if item > 0 and item in numbers:
                        return False
                    numbers.append(item)
        
    return True        
    
def sudoku_grid_correct(sudoku:list):
    if block_correct(sudoku) == True and column_correct(sudoku) == True and row_correct(sudoku) == True:
        return True
    else: 
        return False


if __name__ == "__main__":
    sudoku = [
    [ 2, 0, 1, 9, 8, 0, 4, 0, 3 ],
    [ 8, 0, 0, 6, 3, 0, 0, 0, 0 ],
    [ 6, 4, 3, 0, 0, 0, 5, 9, 8 ],
    [ 3, 1, 6, 7, 5, 0, 0, 4, 0 ],
    [ 8, 4, 9, 3, 1, 6, 0, 7, 0 ],
    [ 0, 0, 0, 8, 4, 9, 0, 3, 0 ],
    [ 1, 0, 3, 0, 0, 0, 0, 4, 6 ],
    [ 5, 9, 7, 4, 0, 0, 3, 1, 2 ],
    [ 4, 6, 8, 1, 2, 0, 7, 0, 0 ],
    ]
    print(sudoku_grid_correct(sudoku))
    
    print(column_correct(sudoku))