'''
https://app.codility.com/demo/results/training5VW4H5-3P7/
Bob is about to go on a trip. But first he needs to take care of his supply of socks. Each sock has its own color. Bob wants to take as many pairs of clean socks as possible (both socks in the pair should be of the same color).

Socks are divided into two drawers: clean and dirty socks. Bob has time for only one laundry and his washing machine can clean at most K socks. He wants to pick socks for laundering in such a way that after washing he will have a maximal number of clean, same-colored pairs of socks. It is possible that some socks cannot be paired with any other sock, because Bob may have lost some socks over the years.

Bob has exactly N clean and M dirty socks, which are described in arrays C and D, respectively. The colors of the socks are represented as integers (equal numbers representing identical colors).


Write a function:

def solution(K, C, D)

that, given an integer K (the number of socks that the washing machine can clean), two arrays C and D (containing the color representations of N clean and M dirty socks respectively), returns the maximum number of pairs of socks that Bob can take on the trip.
'''
def getPairs(S):
    mp = {}
    for s in S:
        if s in mp: mp[s] += 1
        else: mp[s] = 1
    n = 0
    #print(mp)
    for m in mp:
        n += mp[m] // 2
    return n

def solution(K, C, D):
    # Implement your solution here
    # get any K from D
    if(len(D) <= K):
        C += D
        return getPairs(C)
    
    # select K number from D
    combinations = []
    def generate_comb(a_comb, full, start_index):
        if len(a_comb) == K:
            combinations.append(a_comb)
            return
        for i in range(start_index, len(full)):
            generate_comb(a_comb + [full[i]], full[:i] + full[i+1:], i)
    remains = []
    generate_comb(remains, D, 0)
    # print(combinations)
    max_pairs = 0
    for comb in combinations:
        p = getPairs(C + comb)
        max_pairs = max(p, max_pairs)
    return max_pairs
