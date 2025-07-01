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
                if not _valid(sudoku):
                    sudoku[row][col] = 0
                    
    return sudoku



def _Solution_With_Backtracking(sudoku):
    locations = []
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row][col] == 0:
                locations.append([row,col])

    if _Backtracking(sudoku,locations,0,0) is True:
        return sudoku

    return("No se pudo encontrar una solucion")


def _Backtracking_1(sudoku,locations,r,c):
    if _is_It_Solved(sudoku) is False:
        
        if _valid(sudoku) is False:
        #_valid(sudoku) is False:
            r = locations[-1] 
            c = locations[-1]
            for n in range(1,10):#(num,10):
                sudoku[r][c] = n
                if not _valid(sudoku):
                    sudoku[r][c] = 0
                    continue
                if _Backtracking_1(sudoku,locations,r,c):
                    return True
                #Si num hace que _valid(sudoku) sea falso, que pase al siguiente num
            
            #Si num hace que _valid(sudoku) sea verdadero, que se mantenga ese num
    
            locations.pop()#Si ninguna solucion es verdadera, se corrige la anterior
            return _Backtracking_1(sudoku,locations,r,c)    
        return True
    return True

def _Backtracking(sudoku,locations,r=0,c=0):
    if _is_It_Solved(sudoku):
        return True
    
    if not locations:
        return False
    
    r = locations[-1][0]
    c = locations[-1][1]
    for n in range(1,10):#(num,10):
        sudoku[r][c] = n
        if _valid(sudoku):
            #sudoku[r][c] = 0
            #continue
            next_position = locations[:-1]
            if _Backtracking(sudoku,next_position):
                return True
        sudoku[r][c] = 0

            #Si num hace que _valid(sudoku) sea falso, que pase al siguiente num
            
            #Si num hace que _valid(sudoku) sea verdadero, que se mantenga ese num
    
    #locations.pop()#Si ninguna solucion es verdadera, se corrige la anterior
    #return _Backtracking(sudoku,locations,r,c)    
    return False


def _is_It_Solved(sudoku):
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
        break  # sale del ciclo si es válido


print("Sudoku válido generado:\n")
for row in The_sudoku:
    print(row)


print("\nLa solución es:")
solution = _Solution_With_Backtracking(The_sudoku)
for r in solution:
    print(r)
#for row in solution:
#    print(row)



"""       
The_sudoku = _Asudoku()
Asudoku = _valid(The_sudoku)
print(Asudoku, "\n")
for row in range(0,9):
    print(The_sudoku[row])

print("La solucion es:")
print(_Solution_With_Backtracking(The_sudoku))



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


       
