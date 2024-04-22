'''
https://app.codility.com/demo/results/trainingM79TKG-NV8/
[27% passed]
For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function with python and Dynamic programming:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.
'''

def solution(A):
    # Implement your solution here
    N = len(A) 
    if(N < 1): return 0
    B = [abs(i) for i in A]
    B.sort()
    
    target = sum(B) / 2
    # print (B, target)
    min2half = target
    dp = [float('inf')] * (N + 1)
    dp[0] = B[0]
    #
    for j in range(1, N):
        
        for i in range(1, N):
            prev = j - i
            if(prev >= 0):
                dp_new = dp[prev] + B[j]
                if(abs(dp_new - target) < abs(dp[j] - target)):
                    dp[j] = dp_new
                min2half = min(min2half, abs(dp[j] - target))
                if(min2half == 0): return 0
                # print(2, j, i, prev, dp_new, dp)
                if(j == N - 1):
                    dp_new = abs(dp[prev] - B[j])
                    if(abs(dp_new - target) < abs(dp[j] - target)):
                        dp[j] = dp_new
                    min2half = min(min2half, dp[j] / 2)
                    
                    # print(3, j, i, prev, dp_new, dp)
                #
            #print(1, j, i, prev, dp)
        #
    return int(min2half * 2)
