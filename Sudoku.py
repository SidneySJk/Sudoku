import random


sudoku = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]



def _valid(sudoku):
    """
    Returns True if sudoku accomplice all rules of a sudoku, false if else.
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        boolean: True or False.
    """
    
    if _valid_Grid(sudoku):
        if _valid_Row(sudoku):
            if _valid_Column(sudoku):
                return True
            
    return False


   
def _valid_Grid(sudoku):
    """
    Returns True if sudoku accomplice all rules of a sudoku in the inset, false if else.
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        boolean: True or False.
    """

    for block in range(9):
        row = (block//3) * 3
        col = (block%3) * 3
        for num in range(1,10):
            coin = 0
            for r in range(row,row+3):
                
                for c in range(col,col+3):
                    bloque = sudoku[r][c]
                    if bloque == num:
                        coin += 1
                        
                if coin > 1:
                    return False
                             
    return True 


def _valid_Row(sudoku):
    """
    Returns True if sudoku accomplice all rules of a sudoku in a row, false if else.
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        boolean: True or False.
    """
    for row in sudoku:
        for num in range(1,10):
            coin = 0
            for block in row:
                if block == num:
                    coin += 1
            if coin > 1:
                return False
    return True


def _valid_Column(sudoku):
    """
    Returns True if sudoku accomplice all rules of a sudoku in a column, false if else.
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        boolean: True or False.
    """
    for r in range(9):
        for num in range(1,10):
            coin = 0
            for c in range(9):
                if sudoku[c][r] == num:
                    coin += 1
            if coin > 1:
                return False
        
    return True         
        

def _Asudoku():
    """
    Returns a matrix filled with integers between 0 to 9, given a matrix filled with zeros.
    
    Args:
        None.
    
    Returns:
        boolean: True or False.
    """
    for row in range(0,9):
            
        for col in range(0,9):
            if random.random() < 0.2:
                sudoku[row][col] = random.randint(1,9)
                if not _valid(sudoku):
                    sudoku[row][col] = 0
                    
    return sudoku



def _Solution_With_Backtracking(sudoku):
    """
    Checks where all the zeros in the matrix are located, passes a list with the locations to the Bakctracking funtion,
    if the backtracking returns True the funtion will return the solved sudoku, else print a error message.
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        sudoku(array): a solved array of sudoku
        string: "No se pudo encontar una solucion".
    """
    locations = []
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row][col] == 0:
                locations.append([row,col])

    if _Backtracking(sudoku,locations,0,0) is True:
        return sudoku

    return("No se pudo encontrar una solucion")



def _Backtracking(sudoku,locations,r=0,c=0):
    """
    A backtracking that uses a FILO pruning, every block where the zero was located is a branch, if a brach
    is invalid then is cut, else that option is explore deeper until it leads to the answer
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9.
    
    Returns:
        Boolean: True or False.
    """
    if _is_It_Solved(sudoku):
        return True
    
    if not locations:
        return False
    
    r = locations[-1][0]
    c = locations[-1][1]
    for n in range(1,10):
        sudoku[r][c] = n
        if _valid(sudoku):
            next_position = locations[:-1]
            if _Backtracking(sudoku,next_position):
                return True
        sudoku[r][c] = 0
  
    return False


def _is_It_Solved(sudoku):
    """
    Counts the number of zeros in the sudoku, if theres not any zeros left that means is solved, return True, else return False
    
    Args:
        sudoku (array): a array filed with zeros mostly and integers between 1 to 9 or only integers between 1 to 9.
    
    Returns:
        Boolean: True or False
    """
    count = 0
    for row in sudoku:
        for col in row:
            if col == 0:
                count += 1
                
    if count == 0:
        return True
    
    return False           


while True:
    The_sudoku = _Asudoku()
    if _valid(The_sudoku):
        break


print("Sudoku válido generado:\n")
for row in The_sudoku:
    print(row)


print("\nLa solución es:\n")
solution = _Solution_With_Backtracking(The_sudoku)
for r in solution:
    print(r)






       
