'''
https://app.codility.com/demo/results/training46A9K4-Y7W/
[100%]
You are helping a geologist friend investigate an area with mountain lakes. A recent heavy rainfall has flooded these lakes and their water levels have reached the highest possible point. Your friend is interested to know the maximum depth in the deepest part of these lakes.

We simplify the problem in 2-D dimensions. The whole landscape can be divided into small blocks and described by an array A of length N. Each element of A is the altitude of the rock floor of a block (i.e. the height of this block when there is no water at all). After the rainfall, all the low-lying areas (i.e. blocks that have higher blocks on both sides) are holding as much water as possible. You would like to know the maximum depth of water after this entire area is flooded. You can assume that the altitude outside this area is zero and the outside area can accommodate infinite amount of water.

Write a function with python:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum depth of water.

'''
def getBlocks(A):
    blocks = []
    blocks.append([A[0], 0])
    lookforHigh = True
    for i in range(1, len(A)):
        if(lookforHigh):
            if(A[i] >= blocks[-1][0]): 
                blocks.pop()
                blocks.append([A[i], i])
            else:
                blocks.append([A[i], i])
                lookforHigh = False
        else:
            if(A[i] <= blocks[-1][0]): 
                blocks.pop()
                blocks.append([A[i], i])
            else:
                blocks.append([A[i], i])
                lookforHigh = True
    return blocks
def getDepth(blocks, max_depth):
    i = 0
    left_blocks = []
    while(i < len(blocks)):
        #print(1, blocks[i:])
        l = i+1
        floors = []
        while(l < len(blocks) and blocks[l][0] < blocks[i][0]):
            floors.append(blocks[l][0])
            l += 1
            
        # found a lake
        if(l >= len(blocks)):
            for j in range(0, l-i):
                left_blocks.append(blocks[l-1-j])
            #print(4, left_blocks)
            break
        if(len(floors) > 0):
            min_floor = min(floors)
            max_depth = max(max_depth, blocks[i][0]-min_floor)
            # print (3, max_depth)
        i = l

    return max_depth, left_blocks
def solution(A):
    # Implement your solution here
    blocks = []
    
    max_depth = 0
    
    N = len(A)
    if(N < 2): return 0
    
    blocks = getBlocks(A)
    #print(0, blocks)
    max_depth, left_blocks = getDepth(blocks, max_depth)

    while(len(left_blocks) > 1):
        max_depth, left_blocks = getDepth(left_blocks, max_depth)
    return max_depth
