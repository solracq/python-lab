'''
@author: Solrac
'''
import random

def generate_matrix(matrix):
    #matrix = [[] for _ in range(3)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(10, 90)

    return matrix

def print_sum_matrix(matrix):
    total = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{} ".format(matrix[i][j]), end = " ")
            if (j+1)%3 == 0:
                print()
            total += matrix[i][j]
            
    return total

matrix2 = [[3, 2, 5], [8, 7, 1], [9, 3, 4]]
total = print_sum_matrix(matrix2)
print(total)

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = print_sum_matrix(generate_matrix(matrix))
print(total)