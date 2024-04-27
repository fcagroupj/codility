'''
https://app.codility.com/demo/results/trainingZRZZGR-RA7/
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.


'''
def solution(A):
    # Implement your solution here
    N = len(A)
    perm = [0] * (N + 1)
    s = 0
    for i, a in enumerate(A):
        #print(1, i, a, perm)
        if(a > N): return 0  # if too big
        if(perm[a] <= 0): # new one
            s += 1
            
        perm[a] += 1
        if(perm[a] > 1): return 0
        #print(2, i, a, s, perm)
    if(s == N): return 1
    return 0
