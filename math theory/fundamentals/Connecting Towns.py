# https://www.hackerrank.com/challenges/connecting-towns/problem?isFullScreen=true

# Cities on a map are connected by a number of roads. The number of roads between each city
# is in an array and city 0 is the starting location. The number of roads from city 0 to city 1 
# is the first value in the array, from city 1 to city 3 is the second, and so on.
# How many paths are there from city 0 to the last city in the list, modulo 1234567 ?

from functools import reduce
def connectingTowns(n, routes):
    product = reduce(lambda x, y: x * y, routes)
    return product%1234567

