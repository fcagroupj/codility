'''

A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.
'''
########################################
#     https://app.codility.com/demo/results/training7QVUKY-634/
#     84%
def getMaxFlags(n):
    if(n == 1): return 1
    i = 1
    while(i * (i - 1) < n):
        i += 1
    if(i * (i - 1) == n):
        return i
    return i
def peaksValid(A, peaks, flags):
    min_dist = flags
    
    flag_used = 1
    peak_last = peaks[0]
    #print(2, flags, peaks)
    for i in range(1, len(peaks)):
        if(peaks[i] - peak_last >= min_dist):
            peak_last = peaks[i]
            flag_used += 1
            if(flag_used >= flags): 
                break
    #print(3, flag_used, peak_last)
    return flag_used
def solution(A):
    # Implement your solution here
    N = len(A)
    # get peaks, total number is Np
    peaks = []
    for i in range(1, N-1):
        if(A[i-1] < A[i] and A[i] > A[i+1]):
            peaks.append(i)
    Np = len(peaks)
    if(Np < 1): return Np
    # the max flags are chosen
    m_flags_from_A = getMaxFlags(N)
    m_flags = min(Np, m_flags_from_A)
    #print(1, m_flags, Np, m_flags_from_A)
    # suppose to have i flags or less, check if the peaks are existing at the i distance or less
    max_flags = 1
    for i in range(m_flags, 0, -1):
        flag_valid = peaksValid(A, peaks, i)
        max_flags = max(max_flags, flag_valid)
    return max_flags

########################################
#     https://app.codility.com/demo/results/trainingFQJ22V-A48/
#     73%
def solution(A):
    # Implement your solution here
    N = len(A)
    peaks = [0] * (N)
    n_peak = 0
    for i in range(1, N-1):
        if(A[i-1] < A[i] and A[i] > A[i+1]): 
            peaks[i] = 1
            n_peak += 1
    max_flags = 0
    if(n_peak > 0): max_flags = 1
    else: return 0
    # print(1, peaks)
    i = 2
    while(i*i < N):
        i+=1
    while(i >= 2):
        # flags = i, distance = i
        f_set = []
        peak = 0
        while(peak < N):
            if(len(f_set) < 1):
                if(peaks[peak] > 0): 
                    f_set.append(peak)
                    
            else:
                if(peaks[peak] > 0 and peak >= f_set[-1]+i):
                    f_set.append(peak)
                    if(len(f_set) >= i):  return i
                    
            peak += 1
            # print(2, i, peak, f_set)
        # print(3, i, peak, f_set)
        if(len(f_set) >= i):  
            return i  
        i -= 1
    return max_flags
