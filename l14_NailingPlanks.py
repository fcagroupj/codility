'''
https://app.codility.com/demo/results/trainingPAY7KX-SBM/
[50% passed]
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].


Write a function with python:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.
'''
def solution(A, B, C):
    # Implement your solution here
    N = len(A) 
    nailed = [0] * N
    
    for j in range(len(C)):
        for i in range(N):
            if(nailed[i] < 1): 
                if(A[i] <= C[j] and C[j] <= B[i]):
                    nailed[i] = 1
              
        if(sum(nailed) >= N): return j+1
    
    return -1
################
# As a reference at 50% passed too

def solution(A, B, C):
    # Implement your solution here
    N = len(C)  
    C_valid = {}
    for c in C:
        for i in range(len(A)):
            if(A[i] <= c and c<=B[i]):
                if(c in C_valid):  C_valid[c].append(i)
                else: C_valid[c] = [i]
    #print(1, C_valid)
    
    nails = []
    
    for i in range(N):
        if(C[i] in C_valid): 
            nails += C_valid[C[i]]
            if(len(set(nails)) == len(A)): return i+1
        
    return -1
