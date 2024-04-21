'''
https://app.codility.com/demo/results/training6534C4-RPP/
[100% passed]
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.



The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.
'''
def solution(M, A):
    # Implement your solution here
    seen = set()
    count = 0
    start = 0

    for i in range(len(A)):
        #print(i, start, count)
        while A[i] in seen:
            seen.remove(A[start])
            start += 1
        seen.add(A[i])
        count += (i - start + 1)

        if count > 1000000000:
            return 1000000000

    return count
