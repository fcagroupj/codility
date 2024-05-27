'''
https://app.codility.com/demo/results/trainingAT3PSV-26Y/
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

Write a function with python:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

'''
##########################################################
#  https://app.codility.com/demo/results/trainingY2A86J-ZRW/
#
def solution(A, B):
    # Implement your solution here
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def has_same_prime_divisors(a, b):
        gcd_value = gcd(a, b)
        #print(1, a, b, gcd_value)
        while a != 1:
            a_gcd = gcd(a, gcd_value)
            #print(2, a, gcd_value, a_gcd)
            if a_gcd == 1:
                break
            a //= a_gcd
            
        if a != 1:
            return False

        while b != 1:
            b_gcd = gcd(b, gcd_value)
            #print(3, b, gcd_value, b_gcd)
            if b_gcd == 1:
                break
            b //= b_gcd
            
        return b == 1

    count = 0
    for i in range(len(A)):
        if has_same_prime_divisors(A[i], B[i]):
            count += 1
    return count
#####################################
# The below has 61%
def isPrime(n):
    ret = True
    if(n <= 1): return False
    i = 2
    while(i * i <= n):
        if(n % i == 0): return False
        i += 1
    return ret
def getPrimes(n, upper):
    
    l_prime = []
    i = 1
    while(i * i < n ):
        if(n % i == 0): 
            if(isPrime(i)): l_prime.append(i)
            if(isPrime(n // i)): l_prime.append( n // i)
        i += 1
    if(i * i == n ):
        if(isPrime(i)): l_prime.append(i)
    return l_prime

def gcd1(a, b):
    if(a % b == 0): return b
    return gcd1(b, a%b)

def solution(A, B):
    # Implement your solution here
    total = 0
    for i in range(len(A)):
        # g = gcd1(A[i], B[i])
        #print(1, A[i], B[i], 0)
        l_a = getPrimes(A[i], 0)
        l_b = getPrimes(B[i], 0)
        #print(2, l_a, l_b)
        ret = True
        if(len(l_a) == len(l_b)):
            for j in range(len(l_a)):
                if(l_a[j] != l_b[j]): 
                    ret = False
                    break
        else: ret = False
        if(ret): total += 1
    return total
