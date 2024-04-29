'''
https://app.codility.com/demo/results/trainingXU5RY9-YSS/
There are N ropes numbered from 0 to N − 1, whose lengths are given in an array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of rope I on the line is A[I].

We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied together with a knot, and the length of the tied rope is the sum of lengths of both ropes. The resulting new rope can then be tied again.

For a given integer K, the goal is to tie the ropes in such a way that the number of ropes whose length is greater than or equal to K is maximal.

Write a function:

def solution(K, A)

that, given an integer K and a non-empty array A of N integers, returns the maximum number of ropes of length greater than or equal to K that can be created.
'''
def solution(K, A):
    # Implement your solution here
    sum = 0
    count = 0
    for i in range(len(A)):
        sum += A[i]
        if(sum >= K):
            sum = 0
            count += 1
    return count
