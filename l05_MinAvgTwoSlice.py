'''
https://app.codility.com/demo/results/training838FSJ-NY3/
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
'''
def solution(A):
    # Implement your solution here, it works when only consider 2 or 3 numbers
    N = len(A)
    i = 0
    min_avg = float('inf')
    start = 0
    while(i+2 < N):
        avg = min( (A[i] + A[i+1])/2.0, (A[i] + A[i+1] + A[i+2])/3.0 )
        if(avg < min_avg):
            start = i
            min_avg = avg
        i += 1
    avg = (A[-2] + A[-1]) / 2.0
    if(avg < min_avg):
            start = N - 2
    return start

# AS a reference, this silly solution works by 50% at https://app.codility.com/demo/results/trainingZU6HMM-RB5/
def solution(A):
    # Implement your solution here
    N = len(A)
    su = [0]* (N+1)
    su[0] = A[0]
    for i in range(1, N):
        su[i] = su[i-1] + A[i]
    # print(1, su)
    min_ave = float('inf')
    start = 0
    for P in range(N):
        for Q in range(P+1, N):
            avg = (su[Q] - su[P-1]) / (Q-P + 1)
            min_ave = min(min_ave, avg)
            if(min_ave == avg): 
                start = P
                # print(2, P, Q, start, min_ave, avg)
    return start
