'''
https://app.codility.com/demo/results/trainingPD9VMS-P22/
[33% passed]
n array A of points in a 2D plane is given. These points represent a polygon: every two consecutive points describe an edge of the polygon, and there is an edge connecting the last point and the first point in the array.

A set of points in a 2D plane, whose boundary is a straight line, is called a semiplane. More precisely, any set of the form {(x, y) : ax + by ≥ c} is a semiplane. The semiplane contains its boundary.

A polygon is convex if and only if, no line segment between two points on the boundary ever goes outside the polygon.

The convex hull of a finite set of points in a 2D plane is the smallest convex polygon that contains all points in this set. 
If a polygon is concave (that is, it is not convex), it has a vertex which does not lie on its convex hull border. Your assignment is to find such a vertex.

Write a function with python:

def solution(A)

that, given a non-empty array A consisting of N elements describing a polygon, returns −1 if the polygon is convex. Otherwise, the function should return the index of any point that doesn't belong to the convex hull border. Note that consecutive edges of the polygon may be collinear (that is, the polygon might have 180−degrees angles).

To access the coordinates of the K-th point (where 0 ≤ K < N), use the following syntax:

A[K].x to access the x-coordinate,
A[K].y to access the y-coordinate.
'''
from extratypes import Point2D  # library with types used in the task

def checkPosition( p1,  p2,  p3, updown):
    #print(2, p1,  p2,  p3, updown)
    if((p2.x - p1.x) == 0):
        return 0
    if((p2.y - p1.y) == 0):
        if( updown): 
            if(p3.y < p1.y): return -1
            if(p3.y > p1.y): return 1
        return 0
    a = (p2.y - p1.y) / (p2.x - p1.x)
    b = p1.y - p1.x * a
    p3_y = a*p3.x + b
    #print(3, a, b, p3.x, p3.y, p3_y)
    if(p3_y == p3.y): return 0
    elif(updown):
        if(p3_y < p3.y): return 1
        else: return -1
    
    return 0
def getIndex(a, A):
    for i, p in enumerate(A):
        if(a.x == p.x and a.y == p.y): return i
    return -1
def solution(A):
    # Implement your solution here
    l_x = []
    l_y = []
    for a in A:
        l_x.append(a.x)
        l_y.append(a.y)
    min_x, max_x = min(l_x), max(l_x)
    min_y, max_y = min(l_y), max(l_y)

    #print(1, min_x, max_x, min_y, max_y)
    p = []
    
    for a in A:
        if(a.x == max_x ): 
            p.append(a)
            break
    for a in A:
        if(a.y == min_y ): 
            p.append(a)
            break  
    for a in A:
        if(a.x == min_x ): 
            p.append(a)
            break  
    for a in A:
        if(a.y == max_y ): 
            p.append(a)
            break  
    #print(1, p)
    for a in A:      
        if(a.x == min_x or a.x == max_x): pass
        elif(a.y == min_y or a.y == max_y): pass
        else:
            outside = False
            ret = checkPosition(p[0], p[1], a, updown=True)
            if(ret <= 0): 
                outside = True
                continue
            ret = checkPosition(p[1], p[2], a, updown=True)
            if(ret <= 0): 
                outside = True
                continue
            ret = checkPosition(p[2], p[3], a, updown=True)
            if(ret >= 0): 
                outside = True
                continue
            ret = checkPosition(p[3], p[0], a, updown=True)
            if(ret >= 0): 
                outside = True
                continue
            if(not outside): 
                #print(4, a)
                return getIndex(a, A)
    #print(3, p, q)

    return -1
