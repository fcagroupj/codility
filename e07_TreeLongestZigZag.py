'''
https://app.codility.com/demo/results/trainingKSJCTJ-XWK/
[100% passed]
In this problem we consider binary trees. Let's define a turn on a path as a change in the direction of the path (i.e. a switch from right to left or vice versa). A zigzag is simply a sequence of turns (it can start with either right or left). The length of a zigzag is equal to the number of turns.

Note that a zigzag containing only one edge or one node has length 0.
Write a function with python:

def solution(T)

that, given a non-empty binary tree T consisting of N nodes, returns the length of the longest zigzag starting at the root.

A binary tree can be specified using a pointer data structure. Assume that the following declarations are given:

from dataclasses import dataclass, field

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

An empty tree is represented by an empty pointer (denoted by None). A non-empty tree is represented by a pointer to an object representing its root. The attribute x holds the integer contained in the root, whereas attributes l and r hold the left and right subtrees of the binary tree, respectively.

For the purpose of entering your own test cases, you can denote a tree recursively in the following way. An empty binary tree is denoted by None. A non-empty tree is denoted as (X, L, R), where X is the value contained in the root and L and R denote the left and right subtrees, respectively. 
'''
def getVal(t, turns):
    if(t.l is not None): 
        is_turn = 0
        if(t.x[0] == 2): is_turn = 1
        
        if(t.l is not None): 
            t.l.x = [1, t.x[1] + is_turn]
        #print(turns)
        getVal(t.l, turns)
    if(t.r is not None): 
        is_turn = 0
        if(t.x[0] == 1): is_turn = 1
        
        if(t.r is not None): 
            t.r.x = [2, t.x[1] + is_turn]
        #print(turns)
        getVal(t.r, turns)
    if(t.l is None and t.r is None):
        
        turns[4] = max(t.x[1], turns[4])
        
        #print(turns)
    return turns
def solution(T):

    # Implement your solution here
    # [ sum of node, previous turn, left turn, right turn, max turn]
    T.x = [0, 0]
    l_turns = [0, 0, 0, 0, 0]
    getVal(T, l_turns)
        
    #print(l_turns)
    return l_turns[4]
