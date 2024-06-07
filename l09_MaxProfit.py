'''
https://app.codility.com/demo/results/training533V83-HSN/
'''
def solution(A):
    # Implement your solution here
    N = len(A)
    if(N < 1): return 0
    max_profit = 0
    low, high = A[0], A[0]
    for i in range(1, N):
        if(A[i] == A[i-1]):
            pass
        elif(A[i] > A[i-1]):
            high = A[i]
            max_profit = max(max_profit, high-low)
        elif(A[i] < A[i-1]):
            if(A[i] < low):
                low, high = A[i], A[i]
    
    return max_profit
