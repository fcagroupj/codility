'''
https://app.codility.com/demo/results/trainingXSAE49-RT8/
[50% passed]
[100% passed at chrome-extension://bdfcnmeidppjeaggnmidamkiddifkdib/viewer.html?file=https://codility.com/media/train/solution-count-bounded-slices.pdf]
An integer K and a non-empty array A consisting of N integers are given.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.

A bounded slice is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to K. More precisely it is a slice, such that max(A[P], A[P + 1], ..., A[Q]) − min(A[P], A[P + 1], ..., A[Q]) ≤ K.

The goal is to calculate the number of bounded slices.

Write a function with python:

def solution(K, A)

that, given an integer K and a non-empty array A of N integers, returns the number of bounded slices of array A.

If the number of bounded slices is greater than 1,000,000,000, the function should return 1,000,000,000.
'''
def solution(K, A):
    # Implement your solution here
    n = len(A)
    left = 0  # Left pointer of the sliding window
    count = 0  # Total count of bounded slices
    result = 0  # Result to be returned
    
    # Iterate through the array using a right pointer
    for right in range(n):
        # Update the maximum and minimum values in the sliding window
        while left < right and max(A[left:right+1]) - min(A[left:right+1]) > K:
            left += 1
        
        # Count the number of bounded slices ending at the current position
        count += (right - left + 1)
        
        # Update the result while ensuring it doesn't exceed 1,000,000,000
        result = min(count, 1_000_000_000)
    
    return result
