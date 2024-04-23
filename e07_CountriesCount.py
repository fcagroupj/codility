'''
https://app.codility.com/demo/results/training66BWJB-4HZ/
[]
A rectangular map consisting of N rows and M columns of square areas is given. Each area is painted with a certain color.

Two areas on the map belong to the same country if the following conditions are met:

they have the same color;
it is possible to travel from one area to the other orthogonally (that is, by moving only north, south, west or east) without moving over areas of a different color.
The map can be described by a zero-indexed matrix A consisting of N rows and M columns of integers. The color of each area is described by the corresponding element of the matrix. Two areas have the same color if and only if their corresponding matrix elements have the same value.

Write a function with python

def solution(A)

that, given a zero-indexed matrix A consisting of N rows and M columns of integers, returns the number of different countries to which the areas of the map described by matrix A belong.
'''
def hasNeibour(A, B, i, j, dir):
    
    N = len(A)
    M = len(A[0])
    # print(i, j, B)
    # check left
    if(j > 0 and A[i][ j-1] == A[i][ j] and B[i][j-1] < 1): 
        B[i][j-1] = B[i][j] 
        hasNeibour(A, B, i, j-1, 1)
    if(j < M-1 and A[i][ j+1] == A[i][ j] and B[i][j+1] < 1): 
        B[i][j+1] = B[i][j] 
        hasNeibour(A, B, i, j+1, 2)
    if(i > 0 and A[i-1][ j] == A[i][ j] and B[i-1][j] < 1): 
        B[i-1][j] = B[i][j] 
        hasNeibour(A, B, i-1, j, 3)
    if(i < N-1 and A[i+1][ j] == A[i][ j] and B[i+1][j] < 1): 
        B[i+1][j] = B[i][j] 
        hasNeibour(A, B, i+1, j, 4)
    return False

def solution(A):
    # Implement your solution here
    N = len(A)
    M = len(A[0])
    B = []
    for i in range(N):
        B.append([0]*M)
    n_country = 1
    i, j = 0, 0
    for i in range(N):
        for j in range(M):
            if(B[i][j] == 0): 
                B[i][j] = n_country
                n_country += 1
            
                hasNeibour(A, B, i, j, 0)
            # print(1, i, j, B)
    return n_country - 1        
