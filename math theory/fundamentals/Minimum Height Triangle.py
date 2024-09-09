# https://www.hackerrank.com/challenges/lowest-triangle/problem?isFullScreen=true

# Given integers a and b, find the smallest integer h, such that there exists a triangle 
# of height h, base b, having an area of at least a.

import math
def lowestTriangle(trianglebase, area):
    return math.ceil(((area*2)/trianglebase))


# a = 1/2 * h * b
# h = a*2 / b

# math.ceil -> x if x==int(x) else int(x)+1
