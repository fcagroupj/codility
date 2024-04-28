'''
https://app.codility.com/demo/results/training538RDB-D6Q/
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
'''
def solution(A):
    # Implement your solution here
    N = len(A)
    if(N <= 1): return 0
    leader = []
    
    for a in A:
        if(len(leader) < 1): 
            leader.append(a)
            #count += 1
        elif(a == leader[-1]): 
            leader.append(a)
        else:
            leader.pop()
    # print(0, leader)
    if(len(leader) < 1): return 0
    if(A[0] != leader[0]): return 0
    n_equal = 0
    l_n = 1
    r_n = (N - len(leader)) // 2 + len(leader) - 1
    if(r_n > (N-1)//2): n_equal += 1
    #print(1, 0, l_n, r_n, n_equal)
    for i in range(1, N):
        if(A[i] == leader[0]):
            l_n += 1
            r_n -= 1
            
        else:
            pass
        if(l_n > (i+1)//2 and r_n > (N-i-1) // 2): n_equal += 1
        #print(2, i, l_n, r_n, n_equal)
    return n_equal
