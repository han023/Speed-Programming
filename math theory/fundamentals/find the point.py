# https://www.hackerrank.com/challenges/find-point/problem?isFullScreen=true

# find point of referection of point p across point q to be a 180 rotation of point p around q.


def findPoint(px, py, qx, qy):
    # Write your code here
    return [2*qx-px,2*qy-py]


# using formula r=2p-q
# where p is the 2 point and q is the first point