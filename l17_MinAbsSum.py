'''
https://app.codility.com/demo/results/trainingPBB3QG-3FZ/
[90% passed]
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
    if(N <= 0): return 0
    A = [abs(x) for x in A]
    sm = 0
    mx = 0
    for a in A:
        sm += a
        mx = max(mx, a)
    counts = [0] * (mx + 1)
    for a in A:
        counts[a] += 1
    Total = [-1] * (sm + 1)
    Total[0] = 0
    for i in range(1, len(counts)):
        for j in range(len(Total)):
            if(Total[j] >= 0):
                Total[j] = counts[i]
            elif(j - i >= 0 and Total[j-i] > 0):
                Total[j] = Total[j-i] - 1
            #print(1, i, j, Total)
    # print(2, Total)
    result = sm
    for i in range(len(Total)//2 + 1):
        if(Total[i] >= 0 and result > abs(sm - 2*i)):
            result = abs(sm - 2 * i)
    return result
#########################################
# as a reference
# https://app.codility.com/demo/results/trainingM79TKG-NV8/
# [27% passed]
#
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
