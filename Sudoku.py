import random
base = ['cuadricula','cuadricula','cuadricula',
          'cuadricula','cuadricula','cuadricula',
          'cuadricula','cuadricula','cuadricula']

sudoku = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]


def _len(_list):
    num = 0
    for e in _list:
        num += 1
    return num

def _valid(sudoku):
    
    if _valid_Grid(sudoku):
        if _valid_Row(sudoku):
            if _valid_Column(sudoku):
                return True#_valid_Column(sudoku)
            
    return False
"""            
            else:
                return False 
                #print(f"Columna: {_valid_Column(sudoku)}")
        else:
            return False 
            #print(f"Fila: {_valid_Row(sudoku)}")
    else:
        return False 
        #print(f"Cuadricula: {_valid_Grid(sudoku)}")
"""
            
def _valid_Grid(sudoku):
    #x = 3
    #y = 0
    for block in range(9):
        row = (block//3) * 3
        col = (block%3) * 3
        for num in range(1,10):
            coin = 0
            for r in range(row,row+3):
                
                #comp = 0
                
                for c in range(col,col+3):
                    bloque = sudoku[r][c]
                    #print(f"En la fila {r} y Columna {c}, esta el bloque {bloque}, se esta comparando el numero {num}")
                    if bloque == num:
                        coin += 1
                if coin > 1:
                    
                    return False
                    
                #y = x
                #x += 3

    return True 

def _valid_Row(sudoku):
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
    
    for row in range(0,9):
            
        for col in range(0,9):
            if random.random() < 0.2:
                sudoku[row][col] = random.randint(1,9)
    return sudoku

        
The_sudoku = _Asudoku()
Asudoku = _valid(The_sudoku)
print(Asudoku, "\n")
for row in range(0,9):
    print(The_sudoku[row])
"""

while True:
    The_sudoku = _Asudoku()
    Asudoku = _valid(The_sudoku)
    print(f"Resultado de _valid: {Asudoku}") 
    if Asudoku is True:#_valid(The_sudoku):
        print("Sudoku valido: \n")
        for row in range(0,9):
            print(The_sudoku[row])
        break
    
    else:
        
        print("Sudoku Invalido, generando uno nuevo...\n")
        
""" 


       
