'''
https://app.codility.com/demo/results/trainingYEBBEW-HQW/
'''
def solution(A):
    # Implement your solution here
    N = len(A)  
    sum_l2r = [0] * N
    sum_r2l = [0] * N
    sum_l2r[0] = 0
    sum_r2l[-1] = 0
    for i in range(1, N):
        sum_l2r[i] = max(sum_l2r[i-1] + A[i], 0)
    for i in range(N-2, -1, -1):
        sum_r2l[i] = max(sum_r2l[i+1] + A[i], 0)
    max_double = -float('inf')
    for i in range(1, N-1):
        max_double = max(max_double, sum_l2r[i-1] + sum_r2l[i+1])
    
    return max_double
