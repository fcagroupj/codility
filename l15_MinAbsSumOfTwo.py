'''
https://app.codility.com/demo/results/trainingX2R45T-QWA/
[100% passed]
Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.


Write a function with python:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.
'''
def solution(A):
    # Implement your solution here
    N = len(A)
    A.sort()
    
    min_abs_sum = float('inf')
    left, right = 0, N - 1

    while left <= right:
        abs_sum = abs(A[left] + A[right])
        min_abs_sum = min(min_abs_sum, abs_sum)

        if abs_sum == 0:  # If we find a pair with abs sum 0, we can't find a smaller one
            return 0
        elif A[left] + A[right] < 0:
            left += 1
        else:
            right -= 1

    return min_abs_sum
