

'''
@author: Solrac
'''
from random import randint

def create_matrix(n):
    matrix = [[randint(10, 90) for i in range(n)] for j in range(n)]
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()

def spiral_matrix(matrix, endRow, endColumn):
    startRow = 0
    startColumn = 0
    lista = []
    
    while endRow > startRow and endColumn > startColumn:
        for i in range(startColumn, endColumn):
            print(matrix[startRow][i], end=" ")
            lista.append(matrix[startRow][i])
            
        
        startRow += 1
        
        for i in range(startRow, endRow):
            print(matrix[i][endColumn-1], end=" ")
            lista.append(matrix[i][endColumn-1])
            
        endColumn -= 1
        
        if startRow < endRow:
            for i in range(endColumn - 1, startColumn - 1, -1):
                print(matrix[endRow - 1][i], end=" ")
                lista.append(matrix[endRow - 1][i])
            
            endRow -= 1
                
        if startColumn < endColumn:
            for i in range(endRow - 1, startRow - 1, -1):
                print(matrix[i][startColumn], end = " ")
                lista.append(matrix[i][startColumn])
                
            startColumn += 1

    print('\nSPIRAL MATRIX')
    print(lista)   
                
n = 4 
matrix = create_matrix(n)
print_matrix(matrix)
spiral_matrix(matrix, 4, 4)