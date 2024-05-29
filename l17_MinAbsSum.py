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
# https://app.codility.com/demo/results/trainingZZ5JDC-FS6/
# [72% passed]
#
def solution(A):
    # Implement your solution here
    N = len(A)  
    if(N < 1): return 0
    # k = 2
    # dp = [ [] for i in range(N+1)]
    set_dp = set()
    set_dp.add(A[0])
    set_dp.add(-A[0])
    # dp[0] = [A[0], -A[0]]
    for j in range (1, N):
        new_dp = set()
        for a in set_dp:
            new_dp.add(a + A[j])
            new_dp.add(a - A[j])
        set_dp = new_dp
        # print(1, j, set_dp)

    min_val = float('inf')
    for a in set_dp:
        min_val = min(min_val, abs(a))
    return min_val
#########################################
# as a reference
# https://app.codility.com/demo/results/trainingGYUGQ5-2U5/
# [54% passed]
#
def getMinSum(target, source, min_sum):
    if(len(source) < 1):
        min_sum = min(min_sum, abs(target))
        return min_sum
    value = source[0]
    ret1 = getMinSum(target + value, source[1:], min_sum)
    ret2 = getMinSum(target - value, source[1:], min_sum)

    return min(ret1, ret2)
def solution(A):
    # Implement your solution here
    ret = getMinSum(0, A, float('inf'))
    return ret
