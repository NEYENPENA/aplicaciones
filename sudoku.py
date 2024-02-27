"""
Determinar si un  9 x 9es válido. 
Sólo es necesario validar las celdas completadas  de acuerdo con las siguientes reglas:
Chequear que el tablero introducido sea un tablero 9x9.
Cada fila debe contener los dígitos  1-9 sin repetición.
Cada columna debe contener los dígitos  1-9 sin repetición.
Cada uno de los nueve  3 x 3 subcuadros de la cuadricula debe contener los dígitos  1-9 sin repetición.
"""

board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9",]]

class ValidateSudoku:
    def __init__(self, tablero) :
        self.tablero = tablero
        self.lista_invertida = []

    def chequeo_general(self):
        #Chequear que el tablero sea un tablero de 9 x 9
        #assert
        assert len(self.tablero) == 9, "El tablero ingresado no respeta el formato 9 x 9" 
        for fila in self.tablero:
            assert len(fila) == 9, "El tablero ingresado no respeta el formato 9 x 9" 


    def chequeo_filas(self, lista_a_chequear = 'tablero_general'):
        #Chequear que cada una de las filas contenga los dígitos 1-9 sin repetición
        if lista_a_chequear == 'tablero_general':
            lista_a_chequear = self.tablero        
        for fila in lista_a_chequear:
            for elemento in fila:
                if elemento != ".":
                    assert fila.count(elemento) ==1, "El tablero ingresado no es válido"           


    def chequeo_columnas(self):
        #Chequear que cada una de las columnas contenga los dígitos 1-9 sin repetición
        for column_index in range (0,9):
            for row_index in range(0,9):               
                self.lista_invertida.append(self.tablero[row_index][column_index])   

            self.chequeo_filas([self.lista_invertida])

            self.lista_invertida.clear()          

    def chequeo_subcuadros(self):
        # Funcion mayor
        #Chequear que cada uno de los nueve  3 x 3 subcuadros de la cuadricula contenga los dígitos 1-9 sin repetición
        self.chequeo_3_subcuadros(0,3)
        self.chequeo_3_subcuadros(3,6)
        self.chequeo_3_subcuadros(6,9)
        

    def chequeo_3_subcuadros(self,rango1,rango2):
        # Funcion menor
        self.lista_invertida.clear()        
        for column_index in range(0,9):
            if column_index == 3 or column_index == 6:
                self.lista_invertida.clear()
            for row_index in range(rango1,rango2):
                self.lista_invertida.append(self.tablero[row_index][column_index])
                if len(self.lista_invertida) == 9:
                    self.chequeo_filas([self.lista_invertida])                    
                # Chequeo filas

        
                


# Instanciar el objeto
if __name__ == "__main__":                    
    sudoku = ValidateSudoku(board)
    sudoku.chequeo_general()
    sudoku.chequeo_filas()
    sudoku.chequeo_columnas()
    sudoku.chequeo_subcuadros()
    print("El tablero ingresado es válido")