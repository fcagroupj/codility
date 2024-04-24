'''
https://app.codility.com/demo/results/trainingN96D26-W48/
[100% passed]
A string S containing only the letters "A", "B" and "C" is given. The string can be transformed by removing one occurrence of "AA", "BB" or "CC".

Transformation of the string is the process of removing letters from it, based on the rules described above. As long as at least one rule can be applied, the process should be repeated. If more than one rule can be used, any one of them could be chosen.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns any string that can result from a sequence of transformations as described above.
'''
def solution(S):
    # Implement your solution here
    N = len(S)
    if(N < 2): return S
    s = []
    for a in S:
        if(len(s) > 0 and a == s[-1]):
            s.pop() 
        else:
            s.append(a)
    return ''.join(s)
