# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem?isFullScreen=true

# Sherlock is given 2 square tiles, initially both of whose sides have length l placed in an x-y plane. 
# Initially, the bottom left corners of each square are at the origin and their sides are parallel 
# to the axes.

# At t=0, both squares start moving along line y=x (along the positive x and y) with velocities s1 and s2.

# For each querydetermine the time at which the overlapping area of tiles is equal to the query value, queries[i].

import math
def movingTiles(l, s1, s2, queries):
    res=[]
    for query in queries:
        res.append( (l*math.sqrt(2)-math.sqrt(query)*math.sqrt(2))/(abs(s1-s2)) )
    return res


# length of diagnol of square is l*underoot(2) by pythogras therom