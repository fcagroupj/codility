'''
https://app.codility.com/demo/results/trainingWT55Y7-QNN/
[76%]
Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces out of N pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must be greater than or equal to a given threshold X.

Woolly is interested in the number of different ways in which he can build a pen. Pens are considered different if the sets of lengths of their sides are different. For example, a pen of size 1×4 is different from a pen of size 2×2 (although both have an area of 4), but pens of sizes 1×2 and 2×1 are considered the same.

Write a function with python:

def solution(A, X)

that, given an array A of N integers (containing the lengths of the available pieces of fence) and an integer X, returns the number of different ways of building a rectangular pen satisfying the above conditions. The function should return −1 if the result exceeds 1,000,000,000.
'''
def solution(A, X):
    # Implement your solution here
    m = {}
    for a in A:
        if a in m: m[a] += 1
        else: m[a] = 1
    Pens = []
    squares = 0
    for k in m:
        if(m[k] >= 2): Pens.append(k)
        if(m[k] >= 4): 
            if(k*k >= X): squares += 1
    # print(Pens) 
    Pens.sort()
    count = squares
    for i in range(len(Pens)):
        for j in range(i+1, len(Pens)):
            if(Pens[i] * Pens[j] >= X):
                count += len(Pens) - j
                if(count > 1000000000): return -1
                break
    return count
