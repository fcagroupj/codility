'''
https://app.codility.com/demo/results/training9K92XY-PYZ/
[100% passed]
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.


Write a function with python:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.
'''
def count_blocks(max_sum, A):
        blocks = 1
        current_sum = 0
        for num in A:
            current_sum += num
            if current_sum > max_sum:
                blocks += 1
                current_sum = num
        return blocks
def solution(K, M, A):
    # Implement your solution here
    lower_bound = max(A)
    upper_bound = sum(A)

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if count_blocks(mid, A) <= K:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    return lower_bound
