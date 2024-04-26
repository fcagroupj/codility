'''
https://app.codility.com/demo/results/trainingUBCNQN-WTT/

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.
Write a function with python:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.
'''
def calculate_prefix_sums(A):
    # Calculate prefix sums of an array A
    prefix_sums = [0] * len(A)
    prefix_sums[0] = A[0]
    for i in range(1, len(A)):
        prefix_sums[i] = prefix_sums[i - 1] + A[i]
    return prefix_sums
def solution(N, P, Q):
    # Implement your solution here
    primes = [True] * (N+1)
    primes[0] = primes[1] = False
    i = 2
    while(i * i <= N):
        if(primes[i]):
            k = i*i
            while(k <= N):
                primes[k] = False
                k += i
        i += 1

    #print(primes)
    semi_p = [0] * (N+1)
    # Find semiprimes
    for i in range(2, N + 1):
        if primes[i]:
            for j in range(i, N + 1, i):
                if primes[j // i]:
                    semi_p[j] = 1
    # print(semi_p)
    prefix_sums = calculate_prefix_sums(semi_p)
    # Answer the queries
    results = []
    for i in range(len(P)):
        results.append(prefix_sums[Q[i]] - prefix_sums[P[i] - 1])
    return results
