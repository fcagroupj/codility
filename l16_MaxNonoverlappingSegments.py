'''
https://app.codility.com/demo/results/trainingD77ZJR-6ZV/
[100% passed]
Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.


Write a function with python:

def solution(A, B)

that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.
'''
def solution(A, B):
    # Implement your solution here
    if len(A) == 0:
        return 0

    count = 1
    end = B[0]  # Initialize the end of the current selected segment

    for i in range(1, len(A)):
        if A[i] > end:  # If the start of the next segment is after the end of the current selected segment
            count += 1
            end = B[i]  # Update the end of the current selected segment

    return count
