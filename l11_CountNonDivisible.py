'''
https://app.codility.com/demo/results/training3W2PPD-553/
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.


'''
#######################################################################
#  https://app.codility.com/demo/results/trainingHQJYCN-RBY/
#


#######################################################################
# https://app.codility.com/demo/results/training7TEXWR-MKY/
#
def getDivs(n):
    l_div = []
    i = 1
    while(i * i < n):
        if(n % i == 0):
            l_div += [i, n//i]
        i += 1
    if(i * i == n):
        l_div += [i]
    return l_div
def solution(A):
    # Implement your solution here
    N = len(A)
    # put the number and occurances in dict
    dict_n = {}
    for a in A:
        dict_n[a] = dict_n.get(a, 0) + 1
    # print(1, dict_n)
    # list the divisors of each number and calculate the occurances
    dict_div_n = {}
    for key in dict_n:
        dict_div_n[key] = 0
        l_divs = getDivs(key)
        # print(2, key, l_divs)
        for div in l_divs:
            dict_div_n[key] +=  dict_n.get(div, 0)
    # print(3, dict_div_n)
    # calculate each element
    l_non_div = []
    for a in A:
        l_non_div.append(N - dict_div_n[a])
    return l_non_div
#######################################################################    
# only process unique numbers saved in B
# sort B, then the divisors are only in front of the targeting number
def solution(A):
    # Implement your solution here
    N = len(A)
    ans = [N] * N
    counter = {}
    mapper = {}
    
    for i in A:
        if(i in counter): counter[i] += 1
        else: counter[i] = 1   
    for i in range(N):
        if A[i] in mapper:
            ans[i] = mapper[A[i]]
            continue   
        j, m = 1, A[i]
        while j * j <= m:
            if m % j == 0:
                if j in counter:
                    ans[i] -= counter[j]
                if j * j < m and m // j in counter:
                    ans[i] -= counter[m // j]
            j += 1      
        mapper[A[i]] = ans[i]
    return ans
#######################################################################
def solution3(A):
    # Implement your solution here
    N = len(A)
    m = {}
    for a in A:
        if(a in m): m[a] += 1
        else: m[a] = 1
    
    l_no_div = {}
    B = list(set(A))
    B.sort()
    #print(1, m, B)
    l_no_div[B[0]] = N - m[B[0]]
    for i in range(1, len(B)):
        yes_div = 0
        for j in range(i):
            # can be divided, only in front of current number
            if(B[i] % B[j] == 0):  yes_div += m[B[j]]
        no_div = N - yes_div - m[B[i]]
        l_no_div[B[i]] = no_div
        #print(2, i, B[i], yes_div, no_div)
    r_no_div = [0] * N
    for i in range(N):
        r_no_div[i] = l_no_div[A[i]]
    #print(3, r_no_div, l_no_div)
    return r_no_div
#######################################################################
#
def solution2(A):
    N = len(A)
    l_no_div = {}
    for i in range(N):
        no_div = 0
        for j in range(0, N):
            if(i == j): continue
            if(A[i] % A[j] == 0): pass
            else: no_div += 1
        l_no_div.append(no_div)
    return l_no_div
