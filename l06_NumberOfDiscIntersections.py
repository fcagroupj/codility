'''
https://app.codility.com/demo/results/trainingWJ2NU8-82T/

We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.


'''
def solution(A):
    # Implement your solution here
    discs = []
    for i, a in enumerate(A):
        discs.append([i-a, 'in'])
        discs.append([i+a, 'out'])
    discs.sort(key=lambda x: (x[0], x[1]) )
    #print(1, discs)
    d_layers = 0
    n_inters = 0
    for d in discs:
        if(d[1] == 'in'): 
            n_inters += d_layers
            if(n_inters > 10000000): return -1
            d_layers += 1
        else:
            d_layers -= 1
        #print(2, d, d_layers, n_inters)
    return n_inters
