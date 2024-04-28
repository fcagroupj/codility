'''
https://app.codility.com/demo/results/trainingCCHE6A-UXT/
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.


'''
def solution(H):
    # Implement your solution here
    s = []
    blocks = 0
    for h in H:
        if(len(s) < 1): s.append(h) 
        else:
            if(s[-1] == h):
                pass
            elif(h < s[-1]):
                s.append(h)           
                # when turn lower, remove all the peak
                while(len(s) >= 3 and s[-2] > s[-3] and s[-2] > s[-1]):
                    s.pop(-2)
                    blocks += 1
                    while(len(s) >= 2):     # remove the equal height of blocks
                        if(s[-1] == s[-2]): s.pop()
                        else: break
                    # print(2, s)
                
            else:
                s.append(h)             # keep the higher block

        # print(1, s)
    
    return (len(s) + blocks)
