'''
https://app.codility.com/demo/results/trainingP2A3ZE-549/
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.
'''
def solution(N, A):
    # Implement your solution here
    ans = [0] * N
    max_val, val_floor = 0, 0
    for i in A:
        if i == N + 1:
            val_floor = max(val_floor, max_val)
        else:
            ans[i - 1] = ans[i - 1] + 1 if ans[i - 1] >= val_floor else val_floor + 1
            max_val = max(ans[i - 1], max_val)
        # print(i, max_val, val_floor, ans)
    # check all value
    for i in range(N):
        if ans[i] < val_floor:
            ans[i] = val_floor
    return ans
###### AS a reference, a straight way
def solution(N, A):
    # Implement your solution here
    T = [0] * N

    for a in A:
        if(a >= N + 1): 
            m = max(T) 
            T = [m] * N
        else:
            T[a-1] += 1
        #print(a, mp)
    
    return T
