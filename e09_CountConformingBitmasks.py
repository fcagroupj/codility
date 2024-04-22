'''
https://app.codility.com/demo/results/trainingGVX5J7-BJ2/
[46% passed]
In this problem we consider unsigned 30-bit integers, i.e. all integers B such that 0 ≤ B < 230.

We say that integer A conforms to integer B if, in all positions where B has bits set to 1, A has corresponding bits set to 1.

Write a function with python:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.
'''
numbers = []
    inp = [A, B, C]
    
    for x in inp:
        numbers.append(x)
        b_A = bin(x)[2:]
        bits = []
        for i, a in enumerate(b_A):
            if(a == '0'):
                bits.append(i)
    
        #print(1, bits, b_A)
        n_bits = len(bits)
        if(n_bits > 0):
            for k in range(1, 2**n_bits):
                k_b = bin(k)[2:]
                if(len(k_b) < n_bits): 
                    k_b = '0'*(n_bits-len(k_b)) + k_b
                #print(2, k, k_b)
                s = ''
                for i in range(n_bits):
                    if(i == 0):
                        s += b_A[:bits[i]] + k_b[i]
                    else:
                        s += b_A[bits[i-1]+1:bits[i]] + k_b[i]
                s += b_A[bits[-1]+1 :]
                numbers.append(int(s, 2))
                #print(3, k, k_b, s)
    #print( sorted(numbers) )    
    return len(list(set(numbers)))
