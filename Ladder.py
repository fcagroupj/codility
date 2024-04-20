'''
https://app.codility.com/demo/results/trainingBZMNYW-SGQ/
[87% passed]
You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

The number of different ways can be very large, so it is sufficient to return the result modulo 2 powered by P, for a given integer P.

Write a function with python:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2 powered by B[I].
'''

def fab(N):
    if(N < 1): return [0]
    fs = [0] * (N + 1)
    fs[1] = 1
    for i in range(2, N+1):
        fs[i] = fs[i-1] + fs[i-2]
    return fs
def solution(A, B):
    # Implement your solution here
    res = []
    m = A[0]
    for a in A:
        m = max(m, a)
    fabs = fab(m+1)
    for i in range(len(A)):
        res.append(fabs[A[i] + 1] % (pow(2, B[i])))

    return res
