'''
https://app.codility.com/demo/results/trainingYM5WYS-SKA/
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

Write a function with python:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.
'''
def solution(A):
    # Implement your solution here
    # Implement your solution here
    N = len(A)
    if(N <= 2): return 1
    fibonacci = [0, 1]
    # Generate Fibonacci numbers up to N + 1
    while fibonacci[-1] <= N + 1:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    A.append(1) # last is bank
    # Initialize dp array with infinity values
    dp = [float('inf')] * (N + 2)
    # check the 1st jump
    for f in fibonacci[1:]:
        end = f - 1
        if end <= N and A[end] == 1:
            dp[end] = 1
    #print(dp)

    i = 0
    while(i < N):
        if(dp[i] != float('inf') ):
            for f in fibonacci[1:]:
                end = f + i
                if end <= N and A[end] == 1:
                    dp[end] = min(dp[i]+1, dp[end])
            #print(dp)
        i += 1

    if dp[N] == float('inf'):
        return -1
    else:
        return dp[N]
