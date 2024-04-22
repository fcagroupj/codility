'''
https://app.codility.com/demo/results/trainingGVX5J7-BJ2/
[100% passed]
In this problem we consider unsigned 30-bit integers, i.e. all integers B such that 0 ≤ B < 2**30.

We say that integer A conforms to integer B if, in all positions where B has bits set to 1, A has corresponding bits set to 1.

Write a function with python:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.

Write an efficient algorithm for the following assumptions:

A, B and C are integers within the range [0..1,073,741,823].
'''
def supers(number):
    N = 30
    zeros = sum(1 for bit in range(N) if (number >> bit) & 1 == 0)
    return 2**zeros


def solution(a, b, c):
    
    total = supers(a) + supers(b) + supers(c)
    total -= supers(a | b)         # counted twice, remove one
    total -= supers(b | c)         # counted twice, remove one
    total -= supers(a | c)         # counted twice, remove one
    total += supers(a | b | c)     # counted three times, removed three times, add one
